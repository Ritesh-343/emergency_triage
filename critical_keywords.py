
# A compiled (not officially "found") list of words/phrases that commonly appear
# in Indian-English emergency reporting, built from three sources:

# ---- 1. Physical entrapment / structural danger ----
ENTRAPMENT = [
    "trapped", "stuck", "buried", "crushed", "pinned", "can't move",
    "cant move", "not able to move", "collapsed on", "fell on", "under debris",
    "under rubble", "blocked inside", "locked inside", "can't get out",
    "cant get out", "no way out", "phas gaya", "phas gayi", "dab gaya",
    "dab gayi", "andar phas", "nikal nahi", "bahar nahi aa",
]

# ---- 2. Injury / bleeding / physical harm ----
INJURY = [
    "bleed", "blood", "khoon", "khoon nikal", "wound", "gash", "cut deep",
    "fracture", "broken bone", "broken leg", "broken arm", "burn", "burnt",
    "jal gaya", "jal gayi", "scald", "electrocuted", "shock lag gaya",
    "amputat", "severed", "impaled", "internal bleeding", "head injury",
    "spinal injury", "multiple injuries", "seriously injured", "badly hurt",
    "chot lagi", "bahut chot", "gambhir chot",
]

# ---- 3. Breathing / cardiac / medical emergency ----
MEDICAL = [
    "breath", "not breathing", "saans nahi", "saans le nahi",
    "chest pain", "seene mein dard", "heart attack", "dil ka daura",
    "unconscious", "behosh", "collapsed", "seizure", "fits", "convulsion",
    "stroke", "paralysis", "faint", "fainted", "no pulse", "not responding",
    "not waking up", "high fever", "severe pain", "poisoning", "overdose",
    "allergic reaction", "difficulty breathing", "choking", "gala fas gaya",
    "pregnant emergency", "labour pain", "delivery emergency",
    "diabetic emergency", "sugar low", "sugar level gir gaya",
]

# ---- 4. Fire / explosion ----
FIRE_EXPLOSION = [
    "fire", "aag", "aag lag gayi", "blast", "explosion", "explode",
    "cylinder burst", "gas leak", "short circuit", "electric spark",
    "smoke everywhere", "dhuan", "burning smell", "flames", "fire spreading",
]

# ---- 5. Water / flood / drowning ----
WATER_DANGER = [
    "drown", "doob", "doob raha", "doob rahi", "flood", "baadh",
    "water rising", "paani chad raha", "stuck on roof", "swept away",
    "current le gaya", "boat capsized", "boat sank",
]

# ---- 6. Falling / accident / vehicle ----
ACCIDENT = [
    "accident", "hadsa", "collision", "hit by", "run over", "fell from",
    "giri", "gira", "fell down", "vehicle overturned", "car flipped",
    "bike accident", "truck accident", "train accident", "derailed",
]

# ---- 7. Death / dying / critical state ----
CRITICAL_STATE = [
    "dying", "marr raha", "marr rahi", "mar gaya", "mar gayi", "dead body",
    "no signs of life", "not moving at all", "turning blue", "cold to touch",
    "critical condition", "life threatening", "will die", "losing consciousness",
]

# ---- 8. Vulnerable people (raise priority regardless of stated severity) ----
VULNERABLE = [
    "child inside", "kids inside", "baby inside", "infant", "newborn",
    "missing child", "bachcha andar", "bachche andar", "old man fell",
    "elderly stuck", "pregnant woman", "disabled person stuck",
    "wheelchair stuck", "alone and scared",
]

# ---- 9. Urgency / help-seeking phrases (Indian English calling patterns) ----
URGENCY_PHRASES = [
    "please help", "please come fast", "please come quickly", "sir please",
    "madam please", "jaldi aao", "jaldi aaiye", "bachao", "bachao bachao",
    "madad karo", "madad chahiye", "koi madad karo", "emergency please",
    "very urgent", "life is in danger", "please send help", "please send someone",
    "come immediately", "hurry up please", "no time left",
]

# ---- 10. Common phonetic/typo variants seen in real Indian English typing ----
COMMON_MISSPELLINGS = [
    "blooding", "drownend", "unconcious", "bleding", "colapsed", "burnned",
    "seriousli injured", "brething problem", "hart attack", "faintted",
]
CRITICAL_COMMON_HINDI_ENGLISH_KEYWORDS = ["help","please","urgent","emergency","danger","rescue","save","trapped","stuck","accident","crash",
    "attack","fire","flood","earthquake","collapse","injured","bleeding","unconscious","dying","death","killer","gun","knife","explosion",
    "blast","smoke","drowning","choking","suffocating","terrified","scared","afraid","panic","frightened","desperate","critical","serious",
    "disaster","hostage","kidnapped","robbery","thief","violence","scream","crying","shout","nightmare","collapse","distress","bhai","bhaiya","didi",
    "uncle","aunty","sir","madam","jaldi","abhi","turant","bachao","bachaao","bacha lo","please yaar","yaar","arre","arey","oh god","hai bhagwan","bhagwan",
    "ambulance","police","hospital","doctor","ICU","oxygen","injection","medicine","blood","operation","patient","victim","nearby","location","address","colony",
    "society","building","road","highway","signal","station","bridge","village","city","district","state","helpline","control room","NDRF","help","save","rescue",
    "call","come","run","escape","hide","leave","hurry","rush","move","stop","catch","hold","pull","push","scream","shout","cry","bleed","faint","collapse","breathe",
    "choke","drown","burn","fall","jump","climb","survive","protect","defend","attack","kill","die","rescue","report","inform","notify","search","find","locate","reach",
    "evacuate","respond","assist","support","contact","alert","terrified","frightened","scared","anxious","nervous","worried","hopeless","helpless","desperate","horrified",
    "shocked","devastated","disturbed","stressed","trembling","shaking","crying","screaming","yelling","panic","fear","horror","trauma","confusion","uncertainty","danger","unsafe",
    "insecure","vulnerable","threatened","overwhelmed","broken","suffering","painful","miserable","terrified","helplessness","agony","chaos","emergency","critical","unstable","alarming",
    "horrifying","fearful","threatened","risky","dangerous","fatal","life-threatening","plz","pls","asap","omg","wtf","nooo","ahhh","aaa","omggg","plshelp","helpme","saveus","imscared","imdying",
    "cantbreathe","cantmove","hurryup","someonehelp","anybody","anyone","sos","112","100","101","102","108","rip","crying","panicmode","emergencyhelp","saveplease","plscome","dyinghelp","needhelp","callpolice",
    "callambulance","bloodloss","injuredbadly","savehim","saveher","rescueme","trappedinside","burning","collapsing","floodwater","earthquakehit","landslide","roadblock","nosignal","blackout","bachao","jaldi",
    "jaldi karo","bacha lo","bacha lena","mar gaya","mar jaunga","mar rha hu","mar rahi hu","khoon","khoon nikal raha hai","saans","saans nahi aa rahi","dam ghut raha hai","bachche","mummy","papa","maa","pitaji",
    "ghar","bahar","andar","idhar","udhar","dekho","suno","ruk jao","mat jao","koi hai","koi bachao","phone uthao","network nahi hai","current lag gaya","aag lag gayi","gaadi takra gayi","accident ho gaya","hospital le chalo",
    "police bulao","ambulance bulao","doctor bulao","jaldi aao","please aao",
    "meri help karo","mujhe bachao","mujhe bacha lo","mujhe bachaiye","bahut dard ho raha hai","saans ruk rahi hai","main fas gaya hu","hum fas gaye hain"
]
# Combine everything into one flat list for simple substring matching
CRITICAL_KEYWORDS = (
    ENTRAPMENT + INJURY + MEDICAL + FIRE_EXPLOSION + WATER_DANGER +
    ACCIDENT + CRITICAL_STATE + VULNERABLE + URGENCY_PHRASES + COMMON_MISSPELLINGS + CRITICAL_COMMON_HINDI_ENGLISH_KEYWORDS
)

# Remove duplicates while keeping order
CRITICAL_KEYWORDS = list(dict.fromkeys(CRITICAL_KEYWORDS))