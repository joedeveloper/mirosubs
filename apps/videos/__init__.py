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

def format_time(time):
    if time < 0:
        return ''
    t = int(round(time))
    s = t % 60
    s = s > 9 and s or '0%s' % s 
    return '%s:%s' % (t / 60, s)   


class EffectiveSubtitle:
    def __init__(self, subtitle_id, text, start_time, end_time, sub_order):
        self.subtitle_id = subtitle_id
        self.text = text
        self.start_time = start_time
        self.end_time = end_time
        self.sub_order = sub_order

    @classmethod
    def for_subtitle(cls, subtitle):
        return EffectiveSubtitle(
            subtitle.subtitle_id,
            subtitle.subtitle_text,
            subtitle.start_time,
            subtitle.end_time,
            subtitle.subtitle_order)

    @classmethod
    def for_dependent_translation(cls, subtitle, translation):
        return EffectiveSubtitle(
            subtitle.subtitle_id,
            translation.subtitle_text,
            subtitle.start_time,
            subtitle.end_time,
            subtitle.subtitle_order)

    def display_time(self):
        t = self.start_time
        return '' if t < 0 else format_time(t)

    def display_end_time(self):
        t = self.end_time
        return '' if t < 0 else format_time(t)
