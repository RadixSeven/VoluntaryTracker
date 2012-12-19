# Voluntary Tracker Requirements
******

## Roles

There are two main roles: 

* Trackee (the person who is being tracked) 
* Viewer/Supervisor

## Basic Use cases

The following use cases cover the version 1.0 functionality. Just enough to get things off the ground. The format is slightly modified from the standard in that I have the title (a.k.a. Use Case Name) as an h3 above the use case and have named "Application" as "System"

### Tracks Time

<table>
<tr><th>Case #</th>
<td>1</td></tr>

<tr><th>System</th>
<td>Voluntary Tracker</td></tr>

<tr><th>Case Description</th>
<td>The Trackee works and carries out his life, using the tracker app to record what he does on the computer and when he is on the clock and when not.</td></tr>

<tr><th>Primary Actor</th>
<td>Trackee</td></tr>

<tr><th>Preconditions</th>
<td></td></tr>

<tr><th>Trigger</th>
<td></td></tr>

<tr><th>Basic Flow</th>
<td>
<ol>
<li>Trackee starts up computer
</li><li>Trackee opens tracking program (may start automatically).
</li><li>The program appears on the screen but is not tracking. The tracking mode is "off-the-clock"
</li><li>Trackee toggles start tracking to start the tracking.
</li><li>The program sends its first snapshot to the server, marked off-the-clock and as having no connected predecessor. It then chooses the time of its next snapshot. Note that the snapshots all include the title of the active window.
</li><li>Trackee toggles "on-the-clock". (To "on-the-clock: yes")
</li><li>The program sends another snapshot to the server, marked as "on-the-clock" and that tracking has been on since its predecessor snapshot.
</li><li>Trackee works.
</li><li>The time of the next snapshot comes.
</li><li>The program sends another snapshot, marked on-the-clock and that tracking has been on since its predecessor snapshot. The program decides the time of the next snapshot.
</li><li>Trackee toggles "on-the-clock" (to on-the-clock: No)
</li><li>The program sends another snapshot to the server, marked as "off-the-clock" and that tracking has been on since its predecessor snapshot.
</li><li>Trackee plays video games.
</li><li>The time of the next snapshot comes.
</li><li>The program sends another snapshot, marked on-the-clock and that tracking has been on since its predecessor snapshot. The program decides the time of the next snapshot.
</li><li>Trackee toggles "on-the-clock". (To "on-the-clock: Yes")
</li><li>The program sends another snapshot to the server, marked as "on-the-clock" and that tracking has been on since its predecessor snapshot.
</li><li>Trackee works.
</li><li>Trackee toggles "Is Tracking". (To "Is tracking: No")
</li><li>The program sends another snapshot to the server, marked as "on-the-clock" and that tracking has been on since its predecessor snapshot. 
</li><li>Trackee does something he'd rather not remember.
</li><li>The time of the next snapshot comes.
</li><li>The program does nothing
</li><li>Trackee toggles "Is Tracking". (To "Is tracking: Yes")
</li><li>The program sends a snapshot to the server, marked on-the-clock and as having no connected predecessor. It then chooses the time of its next snapshot. Note that the new time setting would not occur if there were still a pending snapshot time.
</li><li>Trackee works.
</li><li>Trackee closes the program.
</li><li>The program sends another snapshot to the server, marked as "on-the-clock" and that tracking has been on since its predecessor snapshot. Then the program closes.
</li>
</td></tr>

<tr><th>Alternate Flows</th>
<td>
<p><b>First use</b></p>

<p>Between opening the tracking program and it appearing on-screen, the program pops up a dialog asking for the google account of the user being tracked and the automatically generated code giving write access to the account. (This code is available on the web client.) The Trackee goes to the web app, logs in, clicks on "display write access code", copies and pastes the code into the dialog box, and clicks OK.
</p>

<p><b>Power failure</b></p>

<p>If the program closes unexpectedly and can't send its snapshot to the server, then the time between snapshots is not tracked - just as if tracking had been turned off at the last snapshot. If the program closes unexpectedly while sending a snapshot, the snapshot is discarded as if it had never been sent. In this way, the program gives a slightly pessimistic estimate of the time spent and what it was spent doing.
</p>

<p><b>Toggle on-the-clock before starting tracking</b></p>

<p>Instead of 4-7, the trackee toggles "on-the-clock" first. The system sends nothing. Then the trackee toggles "start" tracking and the system sends its first snapshot, this one marked "on-the-clock".
</p>
</td></tr>

</table>

###Blank Use Case Template

<table>
<tr><th>Case #</th>
<td></td></tr>

<tr><th>System</th>
<td></td></tr>

<tr><th>Case Description</th>
<td></td></tr>

<tr><th>Primary Actor</th>
<td></td></tr>

<tr><th>Preconditions</th>
<td></td></tr>

<tr><th>Trigger</th>
<td></td></tr>

<tr><th>Basic Flow</th>
<td></td></tr>

<tr><th>Alternate Flows</th>
<td></td></tr>

</table>

