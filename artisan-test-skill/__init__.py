# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

__author__ = 'RatChicken'

LOGGER = getLogger(__name__)

class ArtisanTestSkill(MycroftSkill):

    def __init__(self):
        super(ArtisanTestSkill, self).__init__(name="ArtisanTestSkill")
        
        self.count = 0

    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
    @intent_handler(IntentBuilder("").require("HelloWorldKeyword"))
    def hello_world_intent(self, message):
        #    dialogs/en-us/hello.world.dialog
        self.speak_dialog("hello.world")

    @intent_handler(IntentBuilder("").require("HowAreYouIntent"))
    def how_are_you_intent(self, message):
        self.speak_dialog("how.are.you")

    
    @intent_handler(IntentBuilder("").require("ThankYouKeyword"))
    def thank_you_intent(self, message):
        #    dialogs/en-us/hello.world.dialog
        self.speak_dialog("welcome")

    # def stop(self):
    #    return False

def create_skill():
    return ArtisanTestSkill()
