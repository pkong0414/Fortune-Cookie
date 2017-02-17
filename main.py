#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
    fortune = ["You will work hard in Launch Code.", "You will start on your next project very soon"
                ,"I see you have projects unfinished","Do your best on understanding concepts"]

    index = random.randint(0,3)

    return fortune[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        message = "<strong>" + getRandomFortune() + "</strong>"
        fortune_message = "Your fortune: " + message
        fortune_body = "<p>" + fortune_message + "</p>"

        lucky_num = "<strong>" + str(random.randint(1,100)) + "</strong>"
        fortune_lucky_num = "Your lucky number: " + lucky_num
        fortune_body2 = "<p>" + fortune_lucky_num + "</p>"

        fortune_button = "<a href='.'><button>Get Fortune!</button></a>"

        content = header + fortune_body + fortune_body2 + fortune_button

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug = True)