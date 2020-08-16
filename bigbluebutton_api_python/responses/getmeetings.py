from jxmlease.dictnode import XMLDictNode

from .base import BaseResponse
from ..core.meeting import Meeting

class GetMeetingsResponse(BaseResponse):
    def get_meetings(self):
        meetings = []

        try:
            if self.get_message_key() == "noMeetings":
                return []
        except KeyError:
            pass

        meeting_data = self.get_field("meetings")["meeting"]
        if isinstance(meetings_data, XMLDictNode):
            # There is only one meeting
            meetings_data = [meetings_data]
        
        for meetingXml in meeting_data:
            meetings.append(Meeting(meetingXml))
        return meetings
