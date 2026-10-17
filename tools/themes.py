"""1000点追加分のテーマ一覧。slug|ヒント（英語）。カテゴリーごとに20点ずつのバッチに分ける。
python3 tools/themes.py で件数チェックと data/../tools/themes.json の書き出し"""
import json, glob, sys

T = {}
T['people'] = """person-laughing|laughing out loud with eyes closed
person-embarrassed|blushing and scratching the back of the head
person-worried|worried, sweat drop, hands clasped
person-tired|exhausted, slumped shoulders, sigh puff
person-shy|peeking from behind both hands
person-confused|small question marks floating around the head
person-proud|confident, hands on hips
person-wishing|hands together making a wish, a small star above
person-clapping|clapping hands with tiny motion lines
person-pointing|pointing to the side with one finger
person-ok-sign|arms forming a big circle over the head (OK)
person-x-sign|arms crossed in an X in front of the chest (no)
person-shrugging|shrugging with palms up
person-yawning|big yawn, sleepy eyes
person-hungry|hungry, holding a fork, drool drop
person-in-love|dreamy smile with small hearts floating
person-scared|scared and shivering, wobble lines
person-cheering-pompoms|cheering with pom-poms
person-bye-bye|waving goodbye with a big wave
person-hugging-heart|hugging a big heart shape
grandpa-cane|kind grandfather with a walking cane
grandparents-couple|grandmother and grandfather side by side smiling
family-three|mother, father and a small child together
mother-holding-baby|mother holding a baby in her arms
father-piggyback|father giving a child a piggyback ride
siblings-holding-hands|two small siblings holding hands
couple-holding-hands|young couple holding hands
friends-high-five|two friends doing a high five
child-drawing|child drawing with crayons on paper
girl-hair-ribbon|little girl with a big hair ribbon smiling
teen-headphones|teenager wearing headphones, relaxed
person-reading-book|person reading a book
person-writing-letter|person writing a letter at a desk
person-phone-call|person talking on a smartphone
person-selfie|person taking a selfie with a phone
person-umbrella-rain|person holding an umbrella in the rain
person-walking-dog|person walking a small dog on a leash
person-shopping-bags|person carrying shopping bags
person-shopping-cart|person pushing a shopping cart
person-eating-meal|person eating with a fork, plate in front
person-drinking-water|person drinking a glass of water
person-brushing-teeth|person brushing teeth
person-washing-face|person washing face with water splashes
person-getting-dressed|person pulling on a sweater
person-morning-stretch|person stretching arms up after waking
person-train-strap|commuter holding a train hand strap
person-riding-bicycle|person riding a bicycle
person-wearing-mask|person wearing a face mask
person-wheelchair|person in a wheelchair smiling
person-giving-flowers|person holding out a bouquet
person-receiving-gift|person happily receiving a gift box
person-apologizing|apologizing with hands pressed together
people-whispering|one person whispering to another
people-arguing|two people quarreling with scribble cloud
people-making-up|two people shaking hands to make up
person-volunteer-cleanup|picking up litter with tongs and a bag
person-donation|putting a coin into a donation box
person-voting|putting a paper into a ballot box
people-queue|three people waiting in line
person-lost-map|confused person holding an open map
person-asking-directions|one person pointing the way to another
person-flashlight|person searching with a flashlight
person-peeking-wall|person peeking out from behind a wall
person-sneezing|person sneezing with a burst
person-happy-tears|crying happy tears with a smile
person-determined|determined, clenched fist, sparkle
person-relaxing-tea|relaxing with a cup of tea
person-meditating|sitting cross-legged meditating
person-dancing|person dancing happily
person-whistling|person whistling with music notes
person-nodding|person nodding in agreement, check bubble
person-raising-hand|person raising a hand to ask
person-daydreaming|daydreaming with a thought cloud containing a heart
person-piggy-bank|person putting a coin into a piggy bank
person-empty-wallet|sad person holding an empty wallet
person-running-late|running in a hurry with toast in mouth
person-checking-watch|checking a wristwatch, waiting
person-sleepless|wide awake in bed at night, moon outside
person-hot-fan|hot and sweating, fanning with a hand fan
person-cold-scarf|cold, shivering in a scarf
person-raincoat|child in a raincoat and boots
person-gardening|watering plants with a watering can
person-on-bench|person sitting on a park bench
person-lazy-sofa|lying on a sofa with a phone
friends-laughing|two friends laughing together
friends-group-photo|three friends posing together
person-welcome|welcoming with open arms
person-thank-you-card|holding a card with a heart
person-peace-sign|smiling and making a peace sign
person-opening-present|opening a present with sparkles
pregnant-woman|pregnant woman gently holding her belly
newborn-baby|newborn baby swaddled in a blanket
toddler-first-steps|toddler taking first steps
kid-tantrum|child having a tantrum
kid-sleeping-teddy|child sleeping hugging a teddy bear
grandma-knitting|grandmother knitting with yarn
grandpa-newspaper|grandfather reading a newspaper (no text)
avatar-person|simple round profile avatar of a person
avatar-group|three overlapping profile avatars
person-heart-hands|making a heart shape with hands"""

T['work'] = """police-officer|police officer saluting (no badge text)
pilot|airline pilot with cap
flight-attendant|flight attendant with scarf
train-conductor|train conductor with cap and whistle
bus-driver|bus driver at the steering wheel
taxi-driver|taxi driver with cap
mail-carrier|mail carrier with a letter bag
carpenter|carpenter with a saw and wood plank
electrician|electrician with tools and cable
plumber|plumber with a wrench and pipe
house-painter|painter with roller and paint bucket
gardener|gardener with pruning shears and hedge
fisherman|fisherman holding a fish
baker|baker holding a tray of bread
barista|barista making a latte
waiter|waiter carrying a tray with a cup
cashier|cashier at a register (no numbers)
shop-clerk|shop clerk bowing behind a counter
hairdresser|hairdresser with scissors and comb
florist|florist holding a flower bucket
pharmacist|pharmacist holding a medicine bottle
dentist|dentist with a mirror tool and a big tooth
veterinarian|veterinarian holding a puppy
caregiver|caregiver supporting an elderly person
nursery-teacher|nursery teacher with apron and a small child
librarian|librarian holding books
programmer|programmer at two monitors
designer|designer drawing on a tablet
photographer|photographer with a camera
reporter|reporter holding a microphone
news-anchor|news anchor at a desk
lawyer|lawyer in a suit holding documents
judge|judge with a gavel
accountant|accountant with a calculator and papers
real-estate-agent|real estate agent holding a house key
salesperson|salesperson in a suit holding a brochure
receptionist|receptionist with a desk bell
call-center|call center worker with a headset
security-guard|security guard with a cap
janitor|cleaner with a mop and bucket
factory-worker|factory worker with goggles and gloves
mechanic|mechanic with a wrench next to a tire
astronaut|astronaut in a spacesuit
archaeologist|archaeologist with a brush and a bone
architect|architect holding a blueprint roll
engineer|engineer with a hard hat and a gear
translator|translator between two speech bubbles
tour-guide|tour guide holding a small flag
hotel-concierge|hotel concierge with a bell cap
sushi-chef|sushi chef in a headband
video-creator|video creator in front of a camera and ring light
tailor|tailor with measuring tape
beekeeper|beekeeper in a veil with a honeycomb
zookeeper|zookeeper with a bucket of food
lifeguard|lifeguard with a float
park-ranger|park ranger with a hat
business-meeting|people around a meeting table
presentation|person presenting a chart on a board
handshake-deal|two business people shaking hands
business-team|team of three business people
video-call|laptop showing a video call grid
working-from-home|person working on a laptop at home with a mug
overtime-night|tired worker at desk at night with moon
business-trip|business person with a rolling suitcase
job-interview|job interview across a desk
new-employee|new employee in a fresh suit, nervous smile
promotion-stairs|person climbing stairs with an arrow up
teamwork-puzzle|hands fitting puzzle pieces together
brainstorming|board with sticky notes and a lightbulb
deadline-hourglass|hourglass with a worried face
paperwork-stress|person buried in piles of paper
filing-cabinet|filing cabinet with folders
briefcase|business briefcase
business-cards|two hands exchanging business cards
coffee-break|coffee cup and a cookie on a desk
signing-contract|hand signing a document with a pen
hanko-stamp|Japanese name seal stamp and ink pad (no characters)
coin-stack|stack of gold coins
wallet|leather wallet with a card peeking out
credit-card|credit card (no numbers)
storefront|small shop front with an awning
startup-rocket|rocket launching from a laptop
target-goal|target with an arrow in the center
strategy-chess|chess pieces on a board
falling-chart|bar chart going down with a sad arrow
pie-chart|pie chart with colorful slices
megaphone|megaphone for marketing announcement
customer-support|chat bubbles with a headset
delivery-truck|delivery truck with boxes
warehouse-boxes|warehouse shelves with boxes
factory-conveyor|conveyor belt with boxes
office-building|tall office building
office-desk|office desk with monitor and plant
office-chair|office swivel chair
time-card|time card machine (no numbers)
payday-envelope|pay envelope with coins
retirement-bouquet|retiring worker receiving a bouquet
award-certificate|framed certificate with a ribbon (no text)
it-support|IT support person fixing a computer
event-staff|event staff with a clipboard and cap"""

T['animals'] = """shiba-dog|shiba inu dog
poodle|fluffy poodle
dachshund|dachshund dog
corgi|corgi dog
golden-retriever|golden retriever dog
bulldog|bulldog
cat-sleeping|cat curled up sleeping
black-cat|black cat
kitten-yarn|kitten playing with a yarn ball
guinea-pig|guinea pig
parakeet|budgie parakeet
turtle|small turtle
hedgehog|hedgehog
lizard|gecko lizard
cow|dairy cow
pig|pink pig
sheep|fluffy sheep
horse|horse
goat|goat
hen|hen chicken
rooster|rooster
duck|duck
donkey|donkey
lion|lion with a mane
tiger|tiger
elephant|elephant
giraffe|giraffe
zebra|zebra
hippo|hippopotamus
rhino|rhinoceros
monkey|monkey
gorilla|gorilla
kangaroo|kangaroo with a joey
koala|koala on a branch
sloth|sloth hanging
fox|fox
raccoon|raccoon
deer|deer
squirrel|squirrel holding an acorn
wolf|wolf
polar-bear|polar bear
red-panda|red panda
otter|otter floating on its back
beaver|beaver
bat|cute bat
camel|camel
alpaca|alpaca
mouse|mouse
dolphin|dolphin jumping
whale|whale with a water spout
shark|friendly shark
octopus|octopus
squid|squid
crab|crab
jellyfish|jellyfish
seal|seal
sea-turtle|sea turtle swimming
clownfish|clownfish
pufferfish|pufferfish
starfish|starfish
seahorse|seahorse
sparrow|sparrow
crow|crow
pigeon|pigeon
eagle|eagle
flamingo|flamingo
parrot|parrot
peacock|peacock with open tail
swan|swan
hummingbird|hummingbird at a flower
woodpecker|woodpecker on a tree
butterfly|butterfly
ladybug|ladybug
bee|honey bee
ant|ant carrying a crumb
dragonfly|dragonfly
rhinoceros-beetle|rhinoceros beetle
stag-beetle|stag beetle
caterpillar|caterpillar on a leaf
snail|snail
firefly|firefly glowing
cicada|cicada on a tree
grasshopper|grasshopper
spider|cute spider on a web
snake|friendly snake
crocodile|crocodile
chameleon|chameleon on a branch
dinosaur|friendly dinosaur
penguin-chick|fluffy baby penguin
swallow-bird|swallow bird flying
mole|mole popping out of the ground
lobster|lobster
puppy-kitten-friends|puppy and kitten together
dog-bone|dog holding a bone
cat-box|cat sitting in a cardboard box
bird-nest|bird nest with eggs and a mother bird
fish-school|school of small fish
duckling-line|mother duck with ducklings in a line
paw-print|paw prints
puffin|puffin"""

T['food'] = """strawberry|strawberry
grapes|bunch of grapes
orange|orange
lemon|lemon
watermelon|watermelon slice
peach|peach
cherries|pair of cherries
pineapple|pineapple
melon|melon
kiwi|kiwi fruit cut
pear|pear
mango|mango
blueberries|blueberries
avocado|avocado half
persimmon|persimmon
carrot|carrot
tomato|tomato
broccoli|broccoli
cabbage|cabbage
onion|onion
potato|potato
eggplant|eggplant
cucumber|cucumber
corn|corn on the cob
green-pepper|green bell pepper
mushroom|mushroom
garlic|garlic
daikon-radish|daikon radish
lettuce|lettuce
sweet-potato|sweet potato
pea-pod|pea pod
curry-rice|curry and rice
fried-egg|fried egg
omurice|omelette rice with ketchup heart
spaghetti|spaghetti with tomato sauce
salad-bowl|salad bowl
soup-bowl|bowl of soup
sandwich|sandwich
hot-dog|hot dog
french-fries|french fries
fried-chicken|fried chicken
steak|steak on a plate
tacos|tacos
gyoza|gyoza dumplings
bento-box|bento lunch box
takoyaki|takoyaki
rice-bowl|bowl of rice
miso-soup|miso soup
tempura|shrimp tempura
grilled-fish|grilled fish on a plate
pancakes|stack of pancakes with syrup
croissant|croissant
toast-butter|toast with butter
cereal-bowl|cereal with milk
donut|donut with sprinkles
cupcake|cupcake
cake-slice|strawberry shortcake slice
pudding|custard pudding
macarons|macarons
cookies|cookies
chocolate-bar|chocolate bar
candy|wrapped candies
lollipop|swirl lollipop
popcorn|popcorn
dango|three-color dango
taiyaki|fish-shaped taiyaki
mochi|mochi rice cakes
shaved-ice|shaved ice
parfait|parfait glass
crepe|crepe
green-tea|green tea cup
milk|milk carton (no text)
orange-juice|glass of orange juice
soda|bottle of soda (no label text)
bubble-tea|bubble tea
beer|mug of beer
wine|glass of wine
water-bottle|water bottle
smoothie|smoothie
hot-chocolate|hot chocolate with marshmallows
egg|eggs
cheese|cheese wedge
honey-jar|honey jar with dipper
jam-jar|jam jar
salt-pepper|salt and pepper shakers
nori-roll|sushi rolls
onigiri-set|two rice balls on a plate
udon|udon noodles bowl
fried-rice|fried rice
dumpling-soup|dumpling soup
pizza-whole|whole pizza
burrito|burrito
kebab|meat skewers
pretzel|pretzel
bagel|bagel
waffle|waffle
pie|fruit pie
yogurt|yogurt with fruit
nuts|mixed nuts
cotton-candy|cotton candy"""

T['nature'] = """cloudy|fluffy clouds
thunder-cloud|cloud with lightning
snow-falling|snowflakes falling
wind|wind swirls blowing leaves
storm|storm with heavy rain and wind
heat-sun|blazing hot sun with heat waves
sunrise|sunrise over the horizon
sunset|sunset over the sea
tornado|tornado
snowflake|single snowflake
saturn|ringed planet
shooting-star|shooting star
ufo|flying saucer
comet|comet
full-moon|full moon with a cute face
stars|twinkling stars
rocket|rocket flying in space
sunflower|sunflower
rose|red rose
cherry-blossom|cherry blossom branch
cactus|cactus in a pot
forest|forest of trees
palm-tree|palm tree
pine-tree|pine tree
bamboo|bamboo stalks
four-leaf-clover|four-leaf clover
dandelion|dandelion and fluff
hydrangea|hydrangea
lotus|lotus flower
morning-glory|morning glory
ginkgo-leaf|ginkgo leaves
acorns|acorns
pinecone|pinecone
winter-tree|bare tree with snow
ocean-waves|ocean waves
island|small island with a palm tree
river|river flowing through grass
waterfall|waterfall
volcano|volcano
desert|desert with cactus and sun
lake|lake with reflections
flower-field|field of flowers
rice-paddy|rice paddy field
fire|flame
water-drop|water drop with a face
recycle|recycling arrows
earth-eco|earth with leaves (eco)
rock|rock stone
gem|sparkling gem
seashell|seashell
spring|spring scene with blossoms
summer|summer scene with sun and sea
autumn|autumn scene with red leaves
winter|winter scene with snow
leaf|green leaf
clover-field|grass with clovers
moss-stump|tree stump with moss
cave|cave entrance
cliff-sea|cliff by the sea
hill|green rolling hills
puddle|puddle with ripples
icicle|icicles
sunbeam-clouds|sun peeking from clouds
crescent-moon|crescent moon
milky-way|milky way stars
planet-earth-moon|earth and moon
lavender|lavender
poppy|poppy flowers
daisy|daisy flower
bonsai|bonsai tree
seed|seeds in a hand
mushroom-forest|mushrooms in the forest
snow-mountain|snowy mountain range
aurora|aurora in the sky
coral-reef|coral reef
sea-grass|seaweed and bubbles
weather-umbrella-sun|sun and umbrella (weather forecast)
thermometer-hot|thermometer with sun (no numbers)
thermometer-cold|thermometer with snowflake (no numbers)
wildflowers|wildflowers bouquet"""

T['home'] = """dining-table|dining table with chairs
chair|wooden chair
bookshelf|bookshelf with books
wardrobe|wardrobe
drawers|chest of drawers
mirror|standing mirror
window-curtains|window with curtains
kotatsu|kotatsu heated table
futon|futon bedding
cushion|cushion
refrigerator|refrigerator
microwave|microwave oven
rice-cooker|rice cooker
toaster|toaster with toast popping
kettle|kettle with steam
vacuum-cleaner|vacuum cleaner
robot-vacuum|robot vacuum
air-conditioner|air conditioner
electric-fan|electric fan
heater|space heater
iron|clothes iron
hair-dryer|hair dryer
television|television
ceiling-light|ceiling light
frying-pan|frying pan with egg
cutting-board|knife and cutting board with vegetables
kitchen-utensils|ladle, spatula and whisk
plates|stack of plates
teapot|teapot
oven-mitt|oven mitt
apron|apron
toilet|toilet
toothbrush-cup|toothbrushes in a cup
towel|folded towels
soap|soap with bubbles
shampoo|shampoo bottles (no text)
shower|shower head with water
laundry-hanging|laundry hanging to dry
folding-clothes|folded clothes stack
washing-dishes|washing dishes in a sink
mopping|mop and bucket
window-cleaning|cleaning a window with a spray
taking-out-trash|trash bag at the door
grocery-bag|grocery bag with vegetables
door|front door
intercom|doorbell intercom
mailbox|mailbox with a letter
umbrella-stand|umbrella stand
slippers|pair of slippers
shoes-entrance|shoes at the entrance
picture-frame|picture frame
wall-clock|wall clock (no numbers)
candle|candle
toolbox|toolbox
hammer|hammer and nails
ladder|ladder
flashlight|flashlight
emergency-bag|emergency kit backpack
moving-boxes|moving boxes
apartment|apartment building
desk-chair|study desk and chair
houseplant|large houseplant
air-purifier|air purifier
humidifier|humidifier with mist
dishwasher|dishwasher
sewing-kit|sewing kit
ironing-board|ironing board
coat-rack|coat rack with coat and hat
storage-boxes|storage boxes
garden-hose|garden hose
key-holder|key hooks with keys
light-switch|light switch
power-strip|power strip
smoke-alarm|smoke alarm
fire-extinguisher|fire extinguisher
bath-towel-robe|bathrobe
bunk-bed|bunk bed
baby-crib|baby crib
pet-bed|pet bed with a toy
doormat|doormat (no text)"""

T['tech'] = """desktop-computer|desktop computer
tablet|tablet
smartwatch|smartwatch
headphones|headphones
earbuds|wireless earbuds
keyboard|keyboard
computer-mouse|computer mouse
printer|printer with paper
usb-drive|USB flash drive
server|server rack
vr-headset|VR headset
drone|drone
3d-printer|3D printer
smart-speaker|smart speaker
ai-chat|chat bubble with a sparkle (AI chat)
ai-chip|chip with a brain pattern
coding-screen|screen with code lines (no readable text)
bug-code|cute bug on a screen
settings-gear|settings gear
download|download arrow into a tray
link-chain|chain link
qr-code|QR code pattern
barcode|barcode
password-key|key with dots (password)
fingerprint|fingerprint
face-scan|face recognition frame
shield|security shield with check
virus-alert|warning sign with a virus
spam-mail|envelope with a warning
notification-bell|notification bell with a dot
chat-bubbles|chat bubbles
play-button|video play button
live-stream|camera with a red recording dot
thumbs-up-like|thumbs up icon
comment|comment bubble with dots
database|database cylinders
satellite|satellite
antenna-tower|antenna tower with signal
charging-cable|charging cable
power-plug|power plug and socket
solar-panel|solar panels with sun
ev-charging|electric car charging
online-shopping|shopping cart on a phone
mobile-payment|phone paying at a terminal
gps-phone|phone with a map pin
smart-home|house with wifi and devices
sd-card|SD card
save-disk|floppy disk save icon
cursor-click|mouse cursor clicking
loading|loading spinner
error-warning|warning triangle with exclamation shape
folder|folder with documents
trash-delete|trash can delete icon
photo-gallery|photo icon with mountains
microphone|podcast microphone
game-console|handheld game console
webcam|webcam
cloud-computing|cloud with network nodes
robot-arm|industrial robot arm
smartphone|plain smartphone"""

T['school'] = """eraser|eraser
crayons|crayons
colored-pencils|colored pencils
scissors|scissors
glue|glue stick
watercolors|watercolor paints and brush
pencil-sharpener|pencil sharpener
pencil-case|pencil case
drawing-compass|drawing compass
globe-desk|desk globe
abacus|abacus
test-tubes|test tubes in a rack
magnet|horseshoe magnet with clips
dictionary|thick open dictionary (no text)
school-desk|school desk and chair
blackboard|blackboard with chalk
school-bell|school bell
school-bus|school bus
school-lunch|school lunch tray
recorder-flute|recorder flute
classroom-hands|students raising hands
test-paper|test paper with red circles (no numbers)
homework|homework at a desk
studying-late|studying late at night
entrance-ceremony|entrance ceremony with cherry blossoms
graduation-ceremony|students in graduation gowns
school-uniform|student in a school uniform
field-trip|students on a field trip
library|library shelves and reading table
toy-blocks|toy blocks (no letters)
math-shapes|math shapes triangle circle square
science-experiment|science experiment with flask bubbles
plant-observation|watching a plant with a notebook
bug-catching|insect net and cage
world-map|world map
kindergarten-kids|kindergarten kids playing
kindergarten-hat|kindergarten yellow hat and bag
university-campus|university building
lecture-hall|lecture hall seats
online-class|online class on a laptop
tutor|tutor helping a student
study-group|students studying together
highlighters|highlighter pens
bookmark|book with a bookmark
teacher-grading|teacher grading papers
principal|school principal
school-gate|school gate
clay|modeling clay
origami-class|origami paper and crane
piano-class|small piano in a classroom
pe-class|PE class with a ball
swimming-class|swimming class kids in pool
lunch-time-kids|kids eating lunch
ruler|ruler
notebook-stack|stack of notebooks
backpack-yellow-cover|backpack with rain cover
stopwatch-class|timer on a desk
art-class|easel with a painting
calligraphy-set|calligraphy brush and ink stone
chalk-eraser|blackboard eraser and chalk"""

T['travel'] = """taxi|taxi
police-car|police car
fire-truck|fire truck
truck|truck
motorcycle|motorcycle
scooter|scooter
electric-scooter|electric kick scooter
helicopter|helicopter
subway|subway train
tram|tram
ropeway|ropeway cable car
sailboat|sailboat
canoe|canoe
submarine|submarine
steam-locomotive|steam locomotive
camper-van|camper van
tractor|tractor
traffic-light|traffic light
crosswalk|crosswalk with a person
gas-station|gas station pump
bus-stop|bus stop
train-platform|train station platform
airport|airport terminal with plane
passport|passport booklet (no text)
ticket|travel ticket
luggage-cart|luggage cart
backpacker|backpacker
hotel|hotel building
ryokan|Japanese inn
hot-spring|hot spring with steam
beach-umbrella|beach umbrella and chair
swim-ring|swim ring float
sunglasses|sunglasses
sun-hat|straw sun hat
souvenir|souvenir bag
postcard|postcard with stamp
compass|compass
binoculars|binoculars
hiking-boots|hiking boots
hiker|hiker on a mountain trail
picnic|picnic basket and blanket
barbecue|barbecue grill
japanese-castle|Japanese castle
european-castle|European castle
pagoda|pagoda
torii|torii gate
lighthouse|lighthouse
windmill|windmill
bridge|bridge over water
pyramid|pyramids
cruise-ship|cruise ship
world-trip|globe with a plane circling
duffel-bag|travel duffel bag
tourist-photo|tourist taking a photo
road-trip|car on a winding road
tunnel|tunnel
highway|highway road
train-window|view from a train window
ferry|ferry boat
rental-car-key|car key
map-route|map with a dotted route
tent-stars|tent under the stars
mountain-cabin|mountain cabin
airplane-window|view from an airplane window
check-in-counter|airport check-in counter
travel-pillow|neck pillow
camping-chair|camping chair and lantern
lantern|camping lantern
canoe-lake|canoe on a lake
ski-resort|ski lift
train-ticket-gate|ticket gates
sightseeing-bus|double decker sightseeing bus
hot-air-balloons|several hot air balloons
amusement-park|ferris wheel
roller-coaster|roller coaster
aquarium|aquarium tunnel with fish
zoo-gate|zoo entrance
museum|museum building
tower|city tower
skyline|city skyline"""

T['events'] = """new-year-sunrise|first sunrise of the year
kadomatsu|kadomatsu new year decoration
kagami-mochi|kagami mochi
lucky-bag|lucky bag
setsubun|oni mask and beans
valentine-chocolate|heart chocolate box
hinamatsuri|hina dolls
hanami|picnic under cherry blossoms
easter-eggs|easter eggs in a basket
easter-bunny|bunny with an egg
carnation|carnation for mother's day
fathers-day|necktie gift for father's day
koinobori|carp streamers
tanabata|tanabata bamboo with paper strips (no text)
yukata|person in a yukata
summer-festival|summer festival lanterns
bon-dance|bon dance with drum tower
moon-viewing|moon viewing with dango and susuki grass
harvest|autumn harvest basket
thanksgiving|roast turkey
halloween-ghost|cute ghost
witch-hat|witch hat
trick-or-treat|candy bag for trick or treat
halloween-bat|halloween bat and moon
santa|Santa Claus
reindeer|reindeer
wreath|Christmas wreath
stocking|Christmas stocking
gingerbread|gingerbread man
christmas-candle|Christmas candle with holly
snow-globe|snow globe
lunar-new-year-lantern|red lantern
red-envelope|red envelope
wedding-couple|bride and groom
wedding-cake|wedding cake
wedding-rings|wedding rings
bouquet|bridal bouquet
champagne-toast|champagne glasses toasting
party-hats|party hats
bunting|bunting flags
balloon-bunch|bunch of balloons
confetti|confetti
pinata|piñata
festival-stall|festival food stall
goldfish-scooping|goldfish scooping
candy-apple|candy apple
taiko-drum|taiko drum
carnival-mask|carnival mask
music-festival|music festival stage
sparklers|hand sparklers
kids-birthday|child in a birthday hat with cake
surprise-party|surprise party with a banner (no text)
gift-wrapping|wrapping a gift
invitation|invitation card with a seal
cheers-glasses|glasses clinking
anniversary|anniversary hearts and cake
baby-shower|baby shower balloons and onesie
graduation-party|graduation cap and confetti
sports-day-flags|sports day flags
cultural-festival|school festival stage
fireworks-festival|fireworks over the river
snow-festival|snow sculpture
lantern-floating|floating lanterns on water
christmas-presents|presents under the tree
mochi-pounding|pounding mochi with a wooden mallet
autumn-festival|autumn festival with leaves and lantern
cherry-blossom-party|cherry blossoms and bento
ramune-bottle|ramune soda bottle
cake-candles|cake with candles
present-mountain|pile of presents
party-cracker-kids|kids with party crackers
dance-party|disco ball
award-ceremony|award ceremony with trophy
celebration-banner|garland and stars
thank-you-flowers|flowers with a heart card
countdown-party|party clock with confetti (no numbers)
heart-gift|heart-shaped gift box
leaf-viewing|autumn leaf viewing
summer-vacation|summer vacation with straw hat and watermelon
christmas-cookies|Christmas cookies"""

T['sports'] = """baseball|baseball bat and ball
volleyball|volleyball
american-football|american football
rugby|rugby ball
golf|golf club and ball
table-tennis|table tennis paddle and ball
badminton|badminton racket and shuttlecock
swimming|person swimming
cycling-race|racing cyclist
skiing|skier
snowboarding|snowboarder
ice-skating|ice skater
surfing|surfer on a wave
skateboarding|skateboarder
boxing|boxing gloves
karate|karate kid
judo|judo throw
sumo|sumo wrestlers
kendo|kendo
yoga|person doing yoga
dumbbell|dumbbell workout
push-ups|person doing push-ups
jump-rope|person jumping rope
marathon-finish|runner breaking the finish tape
relay-baton|relay baton handoff
high-jump|high jump
hurdles|hurdles
gymnastics|gymnast
archery|archery target and arrow
bowling|bowling pins and ball
climbing|climbing wall
horse-riding|horse riding
rowing|rowing boat
diving|scuba diver
ice-hockey|ice hockey stick and puck
cricket|cricket bat and ball
cheerleader|cheerleader
referee|referee with a whistle
stopwatch|stopwatch
medals|gold, silver and bronze medals
podium|winners podium
stadium|stadium
sneakers|running shoes
sports-drink|sports drink bottle
stretching|person stretching
warm-up|warm-up exercise
tug-of-war|tug of war
ball-toss|ball toss game
sack-race|sack race
frisbee|frisbee
dodgeball|dodgeball
soccer-goal|soccer goal and ball
basketball-hoop|basketball hoop
tennis-player|tennis player
baseball-player|baseball batter
soccer-player|soccer player kicking
volleyball-player|volleyball player spiking
fencing|fencing
weightlifting|weightlifter
trampoline|trampoline jumping"""

T['health'] = """hospital|hospital building
ambulance|ambulance
stethoscope|stethoscope
thermometer|thermometer
pills|pills and capsules
medicine-bottle|medicine bottle
vaccine|syringe vaccine
bandage|adhesive bandage
first-aid-kit|first aid kit
face-mask|face mask
hand-washing|washing hands with soap
hand-sanitizer|hand sanitizer
gargling|gargling
coughing|person coughing
fever|person with fever and ice pack
headache|person with a headache
stomachache|person with a stomachache
toothache|person with a toothache
flu-in-bed|sick person in bed
hay-fever|person sneezing with pollen
eye-drops|eye drops
eyeglasses|eyeglasses
broken-leg|person with crutches and cast
x-ray|x-ray of a bone
blood-pressure|blood pressure monitor
heart-health|heart with a pulse line
lungs|cute lungs
brain|cute brain
tooth|cute tooth
weight-scale|bathroom scale (no numbers)
height-measure|measuring height
healthy-plate|balanced meal plate
good-sleep|sleeping well with moon
mental-health|person with a calm heart
back-pain|person with back pain
eye-strain|tired eyes at a computer
heatstroke|person with heatstroke under the sun
sunscreen|sunscreen bottle
vitamins|vitamin bottle and fruit
hydration|drinking water to stay hydrated
no-smoking|no smoking sign (symbol only)
germs|cute germs
immune-shield|shield protecting from germs
doctor-patient|doctor talking to a patient
hospital-bed|hospital bed
pharmacy|pharmacy counter
medical-chart|clipboard medical chart (no text)
blood-donation|blood donation bag
checkup|health checkup
walking-support|caregiver helping elderly walk
rehabilitation|rehabilitation exercise
massage|massage
dna|DNA helix
lab-sample|test tube sample
pulse-oximeter|finger pulse oximeter
crutches|crutches
wheelchair|wheelchair
hearing-aid|hearing aid
contact-lens|contact lens case
toothbrush|toothbrush and toothpaste"""

T['hobby'] = """guitar|acoustic guitar
piano|piano
violin|violin
drums|drum set
trumpet|trumpet
singing-mic|person singing with a microphone
karaoke|karaoke room
music-notes|music notes
painting-easel|painting on an easel
sewing-machine|sewing machine
pottery|pottery wheel
fishing|fishing rod and fish
video-game|game controller
board-game|board game with dice
playing-cards|playing cards (no letters)
shogi|shogi board
jigsaw-puzzle|jigsaw puzzle
comic-book|comic book (no text)
movie-theater|movie popcorn and ticket
film-reel|film reel
origami-crane|origami crane
calligraphy|calligraphy brush
flower-arranging|flower arranging
baking|baking cookies
coffee-dripper|pour-over coffee
tea-ceremony|tea ceremony bowl and whisk
model-train|model train
kite|kite flying
telescope|stargazing telescope
woodworking|woodworking tools
ballet|ballerina
magic-hat|magic hat and wand
aquarium-tank|home fish tank
dj|DJ turntable
ukulele|ukulele
saxophone|saxophone
knitting|knitting needles and yarn
camera-hobby|person with a camera
bird-watching|person bird watching
gardening-hobby|vegetable garden planter"""

def main():
    existing = set()
    for f in ['data/illustrations.json'] + sorted(glob.glob('data/items/*.json')):
        existing |= {m['slug'] for m in json.load(open(f))}
    seen, out, bad = set(), [], False
    for cat, block in T.items():
        rows = [l.split('|', 1) for l in block.strip().splitlines()]
        n = len(rows)
        print(cat, n, '' if n % 20 == 0 else 'NOT MULTIPLE OF 20')
        if n % 20: bad = True
        for slug, hint in rows:
            if slug in existing or slug in seen:
                print('  DUP', slug); bad = True
            seen.add(slug); out.append({'cat': cat, 'slug': slug, 'hint': hint})
    print('total', len(out))
    if '--write' in sys.argv and not bad:
        batches, b = [], 11
        for cat in T:
            items = [o for o in out if o['cat'] == cat]
            for i in range(0, len(items), 20):
                batches.append({'batch': f'b{b:02d}' if b < 100 else f'b{b}', 'cat': cat, 'items': items[i:i+20]}); b += 1
        json.dump(batches, open('tools/themes.json', 'w'), ensure_ascii=False, indent=1)
        print('wrote', len(batches), 'batches')

main()
