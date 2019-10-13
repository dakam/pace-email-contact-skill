from mycroft import MycroftSkill, intent_file_handler


class PaceEmailContact(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('contact.email.pace.intent')
    def handle_contact_email_pace(self, message):
        self.speak_dialog('contact.email.pace')


def create_skill():
    return PaceEmailContact()

