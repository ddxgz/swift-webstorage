import os

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from swiftbrowser.forms import CreateContainerForm,  \
    LoginForm, AddACLForm
from swiftbrowser.utils import replace_hyphens, prefix_list, \
    pseudofolder_object_list, get_temp_key, get_base_url, get_temp_url
from swiftbrowser.views import containerview
from disk.forms import FolderForm

from swiftclient import client

# Create your views here.
# def index(request):
#     return HttpResponse('disk index')
container = settings.DISK_CONTAINER

def home(request, prefix=None):
    """ Returns list of all objects in current container. """
    storage_url = request.session.get('storage_url', '')
    auth_token = request.session.get('auth_token', '')

    try:
        meta, objects = client.get_container(storage_url, auth_token,
                                             container, delimiter='/',
                                             prefix=prefix)

    except client.ClientException:
        messages.add_message(request, messages.ERROR, _("Access denied."))
        return redirect(containerview)

    prefixes = prefix_list(prefix)
    pseudofolders, objs = pseudofolder_object_list(objects, prefix)
    base_url = get_base_url(request)
    account = storage_url.split('/')[-1]

    read_acl = meta.get('x-container-read', '').split(',')
    public = False
    required_acl = ['.r:*', '.rlistings']
    if [x for x in read_acl if x in required_acl]:
        public = True

    return render_to_response("diskview.html", {
        'container': container,
        'objects': objs,
        'folders': pseudofolders,
        'session': request.session,
        'prefix': prefix,
        'prefixes': prefixes,
        'base_url': base_url,
        'account': account,
        'public': public},
        context_instance=RequestContext(request))


def create_folder(request, prefix=None):
    """ Creates a pseudofolder (empty object of type application/directory) """
    storage_url = request.session.get('storage_url', '')
    auth_token = request.session.get('auth_token', '')

    form = FolderForm(request.POST)
    if form.is_valid():
        foldername = request.POST.get('foldername', None)
        if prefix:
            foldername = prefix + '/' + foldername
        foldername = os.path.normpath(foldername)
        foldername = foldername.strip('/')
        foldername += '/'

        content_type = 'application/directory'
        obj = None

        try:
            client.put_object(storage_url, auth_token,
                              container, foldername, obj,
                              content_type=content_type)
            messages.add_message(request, messages.INFO,
                                 _("folder created."))
        except client.ClientException:
            messages.add_message(request, messages.ERROR, _("Access denied."))

        if prefix:
            return redirect(home, prefix=prefix)
        return redirect(home)

    return render_to_response('create_folder.html', {
                              'container': container,
                              'prefix': prefix,
                              }, context_instance=RequestContext(request))
