# Universal Subtitles, universalsubtitles.org
# 
# Copyright (C) 2010 Participatory Culture Foundation
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see 
# http://www.gnu.org/licenses/agpl-3.0.html.

from django import template
from videos.forms import SubtitlesUploadForm, PasteTranscriptionForm

register = template.Library()

@register.inclusion_tag('videos/_upload_subtitles.html', takes_context=True)
def upload_subtitles(context, video):
    return {
        'video': video,
        'form': SubtitlesUploadForm(context['user']),
        'user': context['user'],
        'request': context['request']
    }

@register.inclusion_tag('videos/_paste_transcription.html', takes_context=True)    
def paste_transcription(context):
    initial = {}
    if 'language' in context:
        initial['language'] = context['language'].language

    context['form'] = PasteTranscriptionForm(context['user'], initial=initial)
    return context