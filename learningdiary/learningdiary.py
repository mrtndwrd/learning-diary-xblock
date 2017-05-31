"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Dict
from xblock.fragment import Fragment
from django.template import Template, Context


class LearningDiary(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.preferences,
        help="A simple counter, to show something happening",
    )

    # We'll be abusing Scope.preferences to save the diary_entries because
    # that's a user-wide field
    diary_entries = Dict(
        help="A simple store for a cross xblock learning diary",
        scope=Scope.preferences)

    block_ref = String(
        default="diary1", scope=Scope.settings,
        help="A ref for the block",
    )

    # The text in the diary entry field when the user has not entered anything
    # yet
    default_diary_entry = "start typing here"

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the LearningDiary, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/learningdiary.html")

        t = Template(html)

        diary_entry = self.default_diary_entry
        if self.block_ref in self.diary_entries:
            diary_entry = self.diary_entries[self.block_ref]

        c = Context({
            'block_ref': self.block_ref,
            'diary_entry': diary_entry,
            'count': self.count,
            'entries':self.diary_entries
        })
        t.render(c)

        #frag = Fragment(html.format(self=self))
        frag = Fragment(t.render(c))
        frag.add_css(self.resource_string("static/css/learningdiary.css"))
        frag.add_javascript(
            self.resource_string("static/js/src/learningdiary.js"))
        frag.initialize_js('LearningDiary')
        return frag

    def studio_view(self, context=None):
        """
        View for editing which part to show in the XBlock
        """
        html = self.resource_string("static/html/learningdiarysettings.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/learningdiary.css"))
        frag.initialize_js('LearningDiary')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need
    # more than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def update_diary(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        #assert data['hello'] == 'world'

        self.diary_entries[self.block_ref] = "Learning Diary updated"
        return {
            "diary": self.diary_entries[self.block_ref],
            "all_entries": self.diary_entries
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("LearningDiary",
             """<learningdiary/>
             """),
            ("Multiple LearningDiary",
             """<vertical_demo>
                <learningdiary/>
                <learningdiary/>
                <learningdiary/>
                </vertical_demo>
             """),
        ]
