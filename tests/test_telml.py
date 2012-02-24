# -*- coding: utf-8 -*-
import re
import telapi
import unittest
from telapi_helper import telml
from telapi_helper.telml import TwimlException
from telapi_helper.telml import Response

class TelapiTest(unittest.TestCase):
    def strip(self, xml):
        return str(xml)

    def improperAppend(self, verb):
        self.assertRaises(TwimlException, verb.append, telml.Say(""))
        self.assertRaises(TwimlException, verb.append, telml.Gather())
        self.assertRaises(TwimlException, verb.append, telml.Play(""))
        self.assertRaises(TwimlException, verb.append, telml.Record())
        self.assertRaises(TwimlException, verb.append, telml.Hangup())
        self.assertRaises(TwimlException, verb.append, telml.Reject())
        self.assertRaises(TwimlException, verb.append, telml.Redirect())
        self.assertRaises(TwimlException, verb.append, telml.Dial())
        self.assertRaises(TwimlException, verb.append, telml.Conference(""))
        self.assertRaises(TwimlException, verb.append, telml.Sms(""))
        self.assertRaises(TwimlException, verb.append, telml.Pause())

class TestResponse(TelapiTest):

    def testEmptyResponse(self):
        r = Response()
        self.assertEquals(self.strip(r), '<?xml version="1.0" encoding="utf-8"?><Response />')

    def testResponseAddAttribute(self):
        r = Response(foo="bar")
        self.assertEquals(self.strip(r), '<?xml version="1.0" encoding="utf-8"?><Response foo="bar" />')

class TestSay(TelapiTest):

    def testEmptySay(self):
        """should be a say with no text"""
        r = Response()
        r.append(telml.Say(""))
        self.assertEquals(self.strip(r), '<?xml version="1.0" encoding="utf-8"?><Response><Say /></Response>')

    def testSayHelloWorld(self):
        """should say hello monkey"""
        r = Response()
        r.append(telml.Say("Hello World"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Say>Hello World</Say></Response>')

    def testSayFrench(self):
        """should say hello monkey"""
        r = Response()
        r.append(telml.Say(u"nécessaire et d'autres"))
        self.assertEquals(unicode(r),
                          '<?xml version="1.0" encoding="utf-8"?><Response><Say>n&#233;cessaire et d\'autres</Say></Response>')

    def testSayLoop(self):
        """should say hello monkey and loop 3 times"""
        r = Response()
        r.append(telml.Say("Hello Monkey", loop=3))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Say loop="3">Hello Monkey</Say></Response>')

    def testSayLoopWoman(self):
        """should say have a woman say hello monkey and loop 3 times"""
        r = Response()
        r.append(telml.Say("Hello Monkey", loop=3, voice=telml.Say.WOMAN))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Say loop="3" voice="woman">Hello Monkey</Say></Response>')

    def testSayConvienceMethod(self):
        """convenience method: should say have a woman say hello monkey and loop 3 times and be in french"""
        r = Response()
        r.addSay("Hello Monkey", loop=3, voice=telml.Say.MAN, language=telml.Say.FRENCH)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Say language="fr" loop="3" voice="man">Hello Monkey</Say></Response>')

    def testSayAddAttribute(self):
        """add attribute"""
        r = telml.Say("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Say foo="bar" />')

    def testSayBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(telml.Say(""))

class TestPlay(TelapiTest):

    def testEmptyPlay(self):
        """should play hello monkey"""
        r = Response()
        r.append(telml.Play(""))
        r = self.strip(r)
        self.assertEqual(r,'<?xml version="1.0" encoding="utf-8"?><Response><Play /></Response>')

    def testPlayHello(self):
        """should play hello monkey"""
        r = Response()
        r.append(telml.Play("http://hellomonkey.mp3"))
        r = self.strip(r)
        self.assertEqual(r, '<?xml version="1.0" encoding="utf-8"?><Response><Play>http://hellomonkey.mp3</Play></Response>')

    def testPlayHelloLoop(self):
        """should play hello monkey loop"""
        r = Response()
        r.append(telml.Play("http://hellomonkey.mp3", loop=3))
        r = self.strip(r)
        self.assertEqual(r, '<?xml version="1.0" encoding="utf-8"?><Response><Play loop="3">http://hellomonkey.mp3</Play></Response>')

    def testPlayConvienceMethod(self):
        """convenience method: should play hello monkey"""
        r = Response()
        r.addPlay("http://hellomonkey.mp3", loop=3)
        r = self.strip(r)
        self.assertEqual(r, '<?xml version="1.0" encoding="utf-8"?><Response><Play loop="3">http://hellomonkey.mp3</Play></Response>')

    def testPlayAddAttribute(self):
        """add attribute"""
        r = telml.Play("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Play foo="bar" />')

    def testPlayBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(telml.Play(""))

class TestRecord(TelapiTest):

    def testRecordEmpty(self):
        """should record"""
        r = Response()
        r.append(telml.Record())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Record /></Response>')

    def testRecordActionMethod(self):
        """should record with an action and a get method"""
        r = Response()
        r.append(telml.Record(action="example.com", method="GET"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Record action="example.com" method="GET" /></Response>')

    def testRecordMaxlengthFinishTimeout(self):
        """should record with an maxlength, finishonkey, and timeout"""
        r = Response()
        r.append(telml.Record(timeout=4,finishOnKey="#", maxLength=30))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Record finishOnKey="#" maxLength="30" timeout="4" /></Response>')

    def testRecordTranscribeCallback(self):
        """should record with a transcribe and transcribeCallback"""
        r = Response()
        r.append(telml.Record(transcribeCallback="example.com"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Record transcribeCallback="example.com" /></Response>')

    def testRecordMaxlengthFinishTimeout(self):
        """should record with an maxlength, finishonkey, and timeout"""
        r = Response()
        r.addRecord(timeout=4,finishOnKey="#", maxLength=30)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Record finishOnKey="#" maxLength="30" timeout="4" /></Response>')

    def testRecordAddAttribute(self):
        """add attribute"""
        r = telml.Record(foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Record foo="bar" />')

    def testRecordBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(telml.Record())

class TestRedirect(TelapiTest):

    def testRedirectEmpty(self):
        r = Response()
        r.append(telml.Redirect())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Redirect /></Response>')

    def testRedirectMethod(self):
        r = Response()
        r.append(telml.Redirect(url="example.com", method="POST"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Redirect method="POST">example.com</Redirect></Response>')

    def testRedirectMethodGetParams(self):
        r = Response()
        r.append(telml.Redirect(url="example.com?id=34&action=hey", method="POST"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Redirect method="POST">example.com?id=34&amp;action=hey</Redirect></Response>')

    def testAddAttribute(self):
        """add attribute"""
        r = telml.Redirect("",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Redirect foo="bar" />')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(telml.Redirect())


class TestHangup(TelapiTest):

    def testHangup(self):
        """convenience: should Hangup to a url via POST"""
        r = Response()
        r.append(telml.Hangup())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Hangup /></Response>')


    def testHangupConvience(self):
        """should raises exceptions for wrong appending"""
        r = Response()
        r.addHangup()
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Hangup /></Response>')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(telml.Hangup())


class TestReject(TelapiTest):

    def testReject(self):
        """should be a Reject with default reason"""
        r = Response()
        r.append(telml.Reject())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Reject /></Response>')

    def testRejectConvenience(self):
        """should be a Reject with reason Busy"""
        r = Response()
        r.addReject(reason='busy')
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Reject reason="busy" /></Response>')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(telml.Reject())

class TestSms(TelapiTest):

    def testEmpty(self):
        """Test empty sms verb"""
        r = Response()
        r.append(telml.Sms(""))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Sms /></Response>')

    def testBody(self):
        """Test hello world"""
        r = Response()
        r.append(telml.Sms("Hello, World"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Sms>Hello, World</Sms></Response>')

    def testToFromAction(self):
        """ Test the to, from, and status callback"""
        r = Response()
        r.append(telml.Sms("Hello, World", to=1231231234, sender=3453453456,
            statusCallback="example.com?id=34&action=hey"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Sms from="3453453456" statusCallback="example.com?id=34&amp;action=hey" to="1231231234">Hello, World</Sms></Response>')

    def testActionMethod(self):
        """ Test the action and method parameters on Sms"""
        r = Response()
        r.append(telml.Sms("Hello", method="POST", action="example.com?id=34&action=hey"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Sms action="example.com?id=34&amp;action=hey" method="POST">Hello</Sms></Response>')

    def testConvience(self):
        """should raises exceptions for wrong appending"""
        r = Response()
        r.addSms("Hello")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Sms>Hello</Sms></Response>')

    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(telml.Sms("Hello"))

class TestDial(TelapiTest):

    def testDial(self):
        """ should redirect the call"""
        r = Response()
        r.append(telml.Dial("1231231234"))
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Dial>1231231234</Dial></Response>')

    def testConvienceMethod(self):
        """ should dial to a url via post"""
        r = Response()
        r.addDial()
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Dial /></Response>')

    def testAddNumber(self):
        """add a number to a dial"""
        r = Response()
        d = telml.Dial()
        d.append(telml.Number("1231231234"))
        r.append(d)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Dial><Number>1231231234</Number></Dial></Response>')

    def testAddNumberConvience(self):
        """add a number to a dial, convience method"""
        r = Response()
        d = r.addDial()
        d.addNumber("1231231234")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Dial><Number>1231231234</Number></Dial></Response>')

    def testAddConference(self):
        """ add a conference to a dial"""
        r = Response()
        d = telml.Dial()
        d.append(telml.Conference("My Room"))
        r.append(d)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Dial><Conference>My Room</Conference></Dial></Response>')

    def testAddConferenceConvenceMethod(self):
        """ add a conference to a dial, conviently"""
        r = Response()
        d = r.addDial()
        d.addConference("My Room")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Dial><Conference>My Room</Conference></Dial></Response>')

    def testAddAttribute(self):
        """add attribute"""
        r = telml.Conference("MyRoom",foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Conference foo="bar">MyRoom</Conference>')


    def testBadAppend(self):
        """ should raise exceptions for wrong appending"""
        self.improperAppend(telml.Conference("Hello"))


class TestGather(TelapiTest):

    def testEmpty(self):
        """ a gather with nothing inside"""
        r = Response()
        r.append(telml.Gather())
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Gather /></Response>')

    def testNestedSayPlayPause(self):
        """ a gather with a say, play, and pause"""
        r = Response()
        g = telml.Gather()
        g.append(telml.Say("Hey"))
        g.append(telml.Play("hey.mp3"))
        g.append(telml.Pause())
        r.append(g)
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Gather><Say>Hey</Say><Play>hey.mp3</Play><Pause /></Gather></Response>')


    def testNestedSayPlayPauseConvience(self):
        """ a gather with a say, play, and pause"""
        r = Response()
        g = r.addGather()
        g.addSay("Hey")
        g.addPlay("hey.mp3")
        g.addPause()
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Response><Gather><Say>Hey</Say><Play>hey.mp3</Play><Pause /></Gather></Response>')

    def testAddAttribute(self):
        """add attribute"""
        r = telml.Gather(foo="bar")
        r = self.strip(r)
        self.assertEquals(r, '<?xml version="1.0" encoding="utf-8"?><Gather foo="bar" />')

    def testNoDeclaration(self):
        """add attribute"""
        r = telml.Gather(foo="bar")
        self.assertEquals(r.toxml(xml_declaration=False), '<Gather foo="bar" />')

    def testImproperNesting(self):
        """ bad nesting"""
        verb = telml.Gather()
        self.assertRaises(TwimlException, verb.append, telml.Gather())
        self.assertRaises(TwimlException, verb.append, telml.Record())
        self.assertRaises(TwimlException, verb.append, telml.Hangup())
        self.assertRaises(TwimlException, verb.append, telml.Redirect())
        self.assertRaises(TwimlException, verb.append, telml.Dial())
        self.assertRaises(TwimlException, verb.append, telml.Conference(""))
        self.assertRaises(TwimlException, verb.append, telml.Sms(""))

if __name__ == '__main__':
    unittest.main()
