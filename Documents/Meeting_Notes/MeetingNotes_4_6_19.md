## Meeting Notes
### 4/6/2019

#### Entity Class Diatgram

	In progress -- almost done

#### Use Case Diagram

	Updated and committed

#### Card Swipe

	We've decided to adjust our system to have the student enter the last four digits of their FSU card number.

	Paired with the name, that should be enough to allow students to sign in easier.

#### Database

	Weighing the options of trying to do a single database instead of separate. Tinkering with those.

#### Card Reader Testing

	Card reader is functioning. Implementation will be more straightforward than anticipated.

#### Prototype Progress

	Pair and group programming today to get a basic version up an running.

#### Edge Cases

	* Non-FSU students check a box to bypass required last four FSU Card Number intro

	* If sign-in fails; enter email adress.

	* Sign-in will assume that entrant is a student.

	* Non-student/faculty entrants will be asked to enter their email adress to sign in.

#### DOM Judge

	Currently researching documentation to make sure we know everything DOMJudge needs from us.

	DomJudge Requirements:

	* Table of teams with teamid as the internal ID of the team

	* Enabled value that causes team to dissapear when set to 0

	* members are the names of the team members separated by by newlines

	* Room is the location or room of the team

	* Comments can be filled with arbitrary useful information

	* teampage_first_visited and hostname field indicate when/whether/from where a team visited its team web interface

#### Ideas

	* Implementing a room feature that tells students what room their team is assigned to and emails them