# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ConversationPaused, ConversationResumed
from rasa_sdk.forms import FormAction
import logging
from rasa_sdk.events import ReminderScheduled




class ActionUserMessage(FormAction):

    def name(self) -> Text:
        return "form_get_client_message"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill."""

        return ["client_name", "client_email", "client_message"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
        "client_name": [self.from_entity(entity = "client_name", intent="client_name_entry"),],
        "client_message": [self.from_entity(entity="client_message"),self.from_text()]
        }
    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],):

        # Do something dramatically here, like call an API for example lol

        dispatcher.utter_message(' your name is {}'.format(tracker.get_slot("client_name")))
        dispatcher.utter_message(' your email is {}'.format(tracker.get_slot("client_email")))
        dispatcher.utter_message(' your message was {}'.format(tracker.get_slot("client_message")))

        return []
