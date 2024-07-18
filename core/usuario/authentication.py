from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object
from passageindentity import Passage, PassageError

from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

from core.usuario.models import Usuario

PASSAGE_APP_ID = settings.PASSAGE_APP_ID
PASSAGE_API_KEY = settings.PASSAGE_API_KEY
PASSAGE_AUTH_STRATEGY = settings.PASSAGE_AUTH_STRATEGY
