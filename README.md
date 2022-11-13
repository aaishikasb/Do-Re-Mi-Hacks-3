# SoundCatch
Watts in a Sound?

## Inspiration 💡
Usually, when I wear headphones and try to increase the volume of my device, I get a notification if I try to set it too high stating that it may damage my hearing in the long run. The same feature is available on Apple Watch as well called Noise Notifications. I wanted to replicate the same thing for people who don't own an Apple Watch and enjoy listening to loud music without headphones.

## What it does 🧭
SoundCatch is a hardware-based apparatus that notifies the user whenever the background noise crosses a certain threshold which might potentially affect the user's hearing abilities. It is easy to build, easy to use, and very cheap to implement, the perfect DIY noise notification.

## How I built it 🔧
I built SoundCatch by interfacing a Sound Detection Module with a Raspberry Pi 4. The Python file (hosted in the repository) is on the lookout for a trigger at all times which would be any sound loud enough to be detected by the module (the detection level can be lowered or increased by the user by modifying the pot only). Once a trigger is received, a message is sent to the registered user via Twilio notifying them that the background volume is exceeding safe limits.

## Challenges we ran into 🏃‍♂️
Many components that I was planning on using in this project weren't available because of a lockdown due to heavy rains in my area.

## Accomplishments that we're proud of 🏅
 - Finishing the project with limited resources.
 - Connecting to the Pi headlessly was a real headache but I found my way around.

## What we learned 🧠
 - Using different tools to connect to a Pi headlessly.
 - Debugging Twilio errors.

## What's next for SoundCatch ⏭
Would love to continue working on this project and add more components moving forward. I initially had ideas to connect an LCD Screen and show the level of volume but I had a digital module and not an analog one hence it wasn't possible in this iteration. Another interesting addition would be adding state LEDs to notify physically when the Twilio notification is sent.
