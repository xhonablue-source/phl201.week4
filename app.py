import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="Week 4: 85-Question Philosophy Quiz", layout="wide")

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False

# Comprehensive 85-question quiz based on the philosophical content
QUIZ_QUESTIONS = [
    # Nature of Philosophy & Critical Thinking (Questions 1-15)
    {
        "id": 1,
        "question": "What does philosophy literally mean?",
        "options": [
            "The study of wisdom",
            "The love of wisdom", 
            "The pursuit of truth",
            "The analysis of reality"
        ],
        "correct": 1,
        "explanation": "Philosophy comes from the Greek 'philosophia' meaning 'love of wisdom' - philo (love) + sophia (wisdom).",
        "category": "Nature of Philosophy"
    },
    {
        "id": 2,
        "question": "According to the text, what is the primary goal of philosophy?",
        "options": [
            "To win arguments against others",
            "To achieve autonomy by examining fundamental beliefs and encouraging rational thinking",
            "To memorize the thoughts of ancient thinkers",
            "To prove that all knowledge is relative"
        ],
        "correct": 1,
        "explanation": "Philosophy's goal is to help us achieve autonomy by making us more aware of our fundamental beliefs and encouraging us to reason and think through issues for ourselves.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 3,
        "question": "What are the three main traditional fields of philosophy?",
        "options": [
            "Logic, ethics, and politics",
            "Epistemology, metaphysics, and ethics",
            "Theology, science, and morality",
            "Ancient, medieval, and modern"
        ],
        "correct": 1,
        "explanation": "The three main fields are epistemology (study of knowledge), metaphysics (study of reality), and ethics (study of moral principles).",
        "category": "Nature of Philosophy"
    },
    {
        "id": 4,
        "question": "Critical thinking involves:",
        "options": [
            "Always disagreeing with popular opinions",
            "Disciplined thinking that bases beliefs on well-founded evidence and logical reasoning",
            "Criticizing everything without offering alternatives",
            "Following the arguments of authority figures"
        ],
        "correct": 1,
        "explanation": "Critical thinking is disciplined thinking that bases beliefs and actions on well-founded evidence and unbiased logical reasoning, avoiding false generalizations.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 5,
        "question": "What is epistemology primarily concerned with?",
        "options": [
            "The nature of being and existence",
            "Questions of knowledge, truth, and perception",
            "Moral principles and values",
            "Political systems and governance"
        ],
        "correct": 1,
        "explanation": "Epistemology deals with questions of knowledge including its structure, reliability, extent, and kinds; truth; perception; and skepticism.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 6,
        "question": "Metaphysics addresses questions about:",
        "options": [
            "How we should treat other people",
            "What we can know about the world",
            "The most general characteristics of existence and reality",
            "How to construct valid arguments"
        ],
        "correct": 2,
        "explanation": "Metaphysics addresses the most general or ultimate characteristics of existence, including the nature of mind, self, human freedom, God's existence, and the soul's immortality.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 7,
        "question": "According to the text, reasoning is:",
        "options": [
            "Always based on emotions and feelings",
            "The process of thinking by which we draw conclusions from evidence",
            "Only useful in mathematics and science",
            "Something that should be avoided in philosophy"
        ],
        "correct": 1,
        "explanation": "Reasoning is the process of thinking by which we draw conclusions from evidence that supports the conclusion, with premises providing reasons or evidence.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 8,
        "question": "What makes philosophy valuable according to the text?",
        "options": [
            "It guarantees wealth and success",
            "It helps achieve freedom, builds critical thinking, and cultivates awareness",
            "It provides easy answers to all life's questions",
            "It allows people to avoid making difficult decisions"
        ],
        "correct": 1,
        "explanation": "Philosophy is valuable because it helps achieve freedom from unexamined assumptions, builds critical thinking abilities, and cultivates awareness of influences on our thoughts and actions.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 9,
        "question": "The Cave Allegory is found in which of Plato's works?",
        "options": [
            "The Apology",
            "The Republic", 
            "The Phaedo",
            "The Meno"
        ],
        "correct": 1,
        "explanation": "The Allegory of the Cave is one of the best-known passages in The Republic, Plato's work on justice and the ideal state.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 10,
        "question": "What does the text mean by 'cultivating awareness'?",
        "options": [
            "Becoming more sensitive to others' feelings",
            "Developing mindfulness about how our thoughts and actions are influenced by the world around us",
            "Learning to meditate and practice spirituality",
            "Paying more attention to current events"
        ],
        "correct": 1,
        "explanation": "Cultivating awareness means developing mindfulness about how the world around us influences our thoughts and actions, helping us deal with significant influences and remove blinders.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 11,
        "question": "According to the text, what was significant about the Pre-Socratic philosophers?",
        "options": [
            "They were the first to rely purely on religious authority",
            "They made the crucial move from mythological to rational explanations",
            "They rejected all forms of reasoning",
            "They focused only on political questions"
        ],
        "correct": 1,
        "explanation": "The Pre-Socratics made crucial contributions by moving from mythological explanations to searching for new ways of understanding reality through reason.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 12,
        "question": "Thales is significant in philosophy because he:",
        "options": [
            "Proved that everything is made of water",
            "Was among the first to seek a rational, non-mythological explanation for reality",
            "Founded the first philosophy school",
            "Wrote the longest philosophical work"
        ],
        "correct": 1,
        "explanation": "Thales was significant for taking a radically new 'philosophical' approach to reality, seeking rational explanations rather than relying on mythological accounts.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 13,
        "question": "What does it mean for philosophy to be 'embodied' according to Ronke Oke?",
        "options": [
            "Philosophy should only concern physical matters",
            "Philosophy is a practice that should transform how we see our realities",
            "Only people with bodies can do philosophy",
            "Philosophy should reject abstract thinking"
        ],
        "correct": 1,
        "explanation": "For Oke, philosophy as an 'embodied discipline' means it's a transformational practice that can lead us to see our own realities differently through dialogue and engagement.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 14,
        "question": "The text suggests that studying philosophy helps with:",
        "options": [
            "Avoiding all controversial topics",
            "Evaluating arguments and claims that bombard us daily",
            "Always agreeing with authority figures",
            "Never changing our minds about anything"
        ],
        "correct": 1,
        "explanation": "Philosophy helps us evaluate the many claims and arguments that bombard us daily, teaching us to instill strong reasoning skills for navigating persuasion attempts.",
        "category": "Nature of Philosophy"
    },
    {
        "id": 15,
        "question": "According to the text, what makes someone a 'critical thinker'?",
        "options": [
            "Someone who criticizes everything they encounter",
            "Someone who thinks carefully and evaluates reasoning well",
            "Someone who never accepts any claims",
            "Someone who only trusts scientific evidence"
        ],
        "correct": 1,
        "explanation": "A critical thinker is someone who learns to think carefully, reason well, and evaluate the reasoning of others, essential for navigating daily life decisions.",
        "category": "Nature of Philosophy"
    },

    # Socrates and Ancient Philosophy (Questions 16-35)
    {
        "id": 16,
        "question": "Why was Socrates put on trial according to the text?",
        "options": [
            "For stealing money from the state",
            "For corrupting the youth of Athens and not believing in the gods of the state",
            "For supporting Athens' enemies in war",
            "For teaching without a license"
        ],
        "correct": 1,
        "explanation": "Socrates was charged with corrupting the youth of Athens and with not believing in the gods of the state, accusations that stemmed from his persistent questioning.",
        "category": "Socrates"
    },
    {
        "id": 17,
        "question": "What was Socrates' response to the Oracle at Delphi saying he was the wisest person?",
        "options": [
            "He immediately accepted this as proof of his superiority",
            "He tested this by questioning people who claimed to have knowledge",
            "He rejected the Oracle as false",
            "He stopped doing philosophy altogether"
        ],
        "correct": 1,
        "explanation": "Socrates tested the Oracle's claim by questioning politicians, poets, and craftsmen, discovering that while they thought they knew things, they actually didn't, leading him to conclude his wisdom lay in knowing that he didn't know.",
        "category": "Socrates"
    },
    {
        "id": 18,
        "question": "Socrates' method of questioning is designed to:",
        "options": [
            "Prove that he is smarter than everyone else",
            "Show people that they don't really know what they think they know",
            "Teach specific facts about the world",
            "Win debates against opponents"
        ],
        "correct": 1,
        "explanation": "Socrates' questioning method aims to expose ignorance and show people that they don't actually know what they think they know, thereby encouraging genuine inquiry.",
        "category": "Socrates"
    },
    {
        "id": 19,
        "question": "In the Apology, what does Socrates say about his mission?",
        "options": [
            "To become wealthy and famous",
            "To questioning people's wisdom and exposing ignorance as a service to the god",
            "To overthrow the Athenian government",
            "To establish a new religion"
        ],
        "correct": 1,
        "explanation": "Socrates sees his mission as a divine service - questioning people's claimed wisdom to expose ignorance and encourage genuine seeking of knowledge.",
        "category": "Socrates"
    },
    {
        "id": 20,
        "question": "According to Socrates in the Crito, why shouldn't he escape from prison?",
        "options": [
            "Because escape is physically impossible",
            "Because he has an obligation to obey the laws that gave him life and education",
            "Because he wants to become a martyr",
            "Because his friends refuse to help him"
        ],
        "correct": 1,
        "explanation": "Socrates argues he has an obligation to obey the government that gave him birth, raised him, and educated him, making escape a form of disobedience to those who benefited him.",
        "category": "Socrates"
    },
    {
        "id": 21,
        "question": "In his trial defense, Socrates compares himself to:",
        "options": [
            "A wise teacher",
            "A gadfly that stings the state into action",
            "A military general",
            "A religious prophet"
        ],
        "correct": 1,
        "explanation": "Socrates compares himself to a gadfly that stings the lazy horse (Athens) into action, suggesting his questioning serves to stimulate the city to examine itself.",
        "category": "Socrates"
    },
    {
        "id": 22,
        "question": "What does Socrates mean when he says 'the unexamined life is not worth living'?",
        "options": [
            "Life without scientific study is meaningless",
            "A life without philosophical self-reflection lacks value",
            "Only philosophers should be allowed to live",
            "People should constantly worry about their lives"
        ],
        "correct": 1,
        "explanation": "Socrates believes that a life without philosophical examination and self-reflection is not worth living - we must question our beliefs and assumptions to live meaningfully.",
        "category": "Socrates"
    },
    {
        "id": 23,
        "question": "In the dialogue with Meletus, Socrates demonstrates:",
        "options": [
            "That he is guilty of the charges",
            "How to win an argument through force",
            "The logical inconsistencies in his accuser's position",
            "That the gods don't exist"
        ],
        "correct": 2,
        "explanation": "Socrates shows that Meletus's accusations are logically inconsistent - Meletus claims Socrates corrupts youth but also that everyone except Socrates improves them, which is contradictory.",
        "category": "Socrates"
    },
    {
        "id": 24,
        "question": "Socrates argues that if he corrupts the youth, he must be doing so:",
        "options": [
            "Intentionally, because he enjoys being evil",
            "Unintentionally, because no one would intentionally harm those they live among",
            "With the help of other philosophers",
            "Only when forced by the government"
        ],
        "correct": 1,
        "explanation": "Socrates argues that if he corrupts youth, it must be unintentional, because no rational person would intentionally corrupt those they must live among, as this would harm themselves.",
        "category": "Socrates"
    },
    {
        "id": 25,
        "question": "What does Socrates' questioning of various Athenians reveal?",
        "options": [
            "That he is the wisest person in Athens",
            "That many people think they know things they don't actually know",
            "That knowledge is impossible to achieve",
            "That only craftsmen have real knowledge"
        ],
        "correct": 1,
        "explanation": "Socrates' questioning reveals that many people, including politicians and poets, think they have knowledge when they don't, highlighting the problem of false confidence in one's understanding.",
        "category": "Socrates"
    },
    {
        "id": 26,
        "question": "In the Crito, what are Socrates' main arguments for not escaping?",
        "options": [
            "Escape would be physically dangerous",
            "The government is like a parent, he has made an agreement to obey, and disobeying would be wrong",
            "He doesn't have enough money to escape",
            "His friends would be punished"
        ],
        "correct": 1,
        "explanation": "Socrates presents three arguments: the government is like a parent who gave him life, he has an implicit agreement to obey the laws, and breaking this agreement would be morally wrong.",
        "category": "Socrates"
    },
    {
        "id": 27,
        "question": "How does Socrates respond to Crito's argument that people will think badly of Crito if Socrates doesn't escape?",
        "options": [
            "He agrees that public opinion is very important",
            "He argues that we should care about the opinions of wise people, not the many",
            "He says Crito should ignore all opinions",
            "He suggests they should take a vote"
        ],
        "correct": 1,
        "explanation": "Socrates argues that we should care about the opinions of those with knowledge (the wise), not the opinions of the many who lack understanding about right and wrong.",
        "category": "Socrates"
    },
    {
        "id": 28,
        "question": "What is the significance of Socrates' claim that he knows nothing?",
        "options": [
            "It shows he is being falsely modest",
            "It demonstrates intellectual humility and the beginning of true wisdom",
            "It proves that knowledge is impossible",
            "It means he never studied anything"
        ],
        "correct": 1,
        "explanation": "Socrates' claim to know nothing represents intellectual humility - recognizing the limits of one's knowledge is the beginning of wisdom and genuine philosophical inquiry.",
        "category": "Socrates"
    },
    {
        "id": 29,
        "question": "Why does Socrates compare his questioning to midwifery?",
        "options": [
            "Because he delivers babies",
            "Because he helps people give birth to ideas they already have within them",
            "Because he only talks to women",
            "Because he works in hospitals"
        ],
        "correct": 1,
        "explanation": "Like a midwife helps deliver babies, Socrates helps people 'give birth' to knowledge and insights they already possess but haven't recognized, through careful questioning.",
        "category": "Socrates"
    },
    {
        "id": 30,
        "question": "What does the text suggest about Socrates' impact on philosophy?",
        "options": [
            "He had no lasting influence",
            "He is considered the father of Western philosophy through his method of questioning",
            "He only influenced ancient Greek thought",
            "He discouraged others from doing philosophy"
        ],
        "correct": 1,
        "explanation": "Socrates is considered the father of Western philosophy because his method of systematic questioning and examination of fundamental assumptions established the foundation for philosophical inquiry.",
        "category": "Socrates"
    },
    {
        "id": 31,
        "question": "According to the text, what was revolutionary about Socrates' approach?",
        "options": [
            "He was the first person to think about ethics",
            "He turned philosophy from natural science toward ethics and human concerns",
            "He invented formal logic",
            "He rejected all previous philosophical ideas"
        ],
        "correct": 1,
        "explanation": "Socrates revolutionized philosophy by turning it away from natural science and cosmology toward ethical questions and human concerns like how we should live.",
        "category": "Socrates"
    },
    {
        "id": 32,
        "question": "In Socrates' view, what is the relationship between knowledge and virtue?",
        "options": [
            "Knowledge and virtue are completely unrelated",
            "True knowledge leads to virtuous action - no one does wrong willingly",
            "Virtue is more important than knowledge",
            "Knowledge corrupts virtue"
        ],
        "correct": 1,
        "explanation": "Socrates believed that true knowledge leads to virtue - if people really understood what was good, they would act virtuously. Evil actions stem from ignorance of the good.",
        "category": "Socrates"
    },
    {
        "id": 33,
        "question": "What does Socrates' willingness to die for his principles demonstrate?",
        "options": [
            "That he was mentally unstable",
            "His commitment to living an examined life and philosophical integrity",
            "That he wanted to become famous",
            "That he hated Athens"
        ],
        "correct": 1,
        "explanation": "Socrates' willingness to die rather than abandon his mission shows his deep commitment to philosophical principles and the examined life he advocated.",
        "category": "Socrates"
    },
    {
        "id": 34,
        "question": "How does Socrates use analogies in his arguments?",
        "options": [
            "To confuse his opponents",
            "To clarify complex ideas by comparing them to familiar situations",
            "To show off his rhetorical skills",
            "To avoid giving direct answers"
        ],
        "correct": 1,
        "explanation": "Socrates uses analogies (like the horse trainer, parent-child relationships) to help clarify abstract philosophical points by connecting them to familiar, concrete situations.",
        "category": "Socrates"
    },
    {
        "id": 35,
        "question": "What is the main lesson of Socrates' life and death according to the text?",
        "options": [
            "That philosophy is dangerous and should be avoided",
            "That we should question our assumptions and live according to our principles",
            "That governments are always wrong",
            "That wisdom is impossible to achieve"
        ],
        "correct": 1,
        "explanation": "Socrates' life demonstrates the importance of questioning our assumptions, examining our beliefs, and having the courage to live according to our principles even when it's difficult.",
        "category": "Socrates"
    },

    # Human Nature and Darwin (Questions 36-55)
    {
        "id": 36,
        "question": "What is the 'Traditional Western View' of human nature?",
        "options": [
            "Humans are essentially animals with no special properties",
            "Humans are rational beings with immaterial souls designed for a purpose",
            "Humans are purely physical machines",
            "Humans are naturally evil"
        ],
        "correct": 1,
        "explanation": "The Traditional Western View, influenced by Greek philosophy and Christianity, holds that humans are rational beings with immaterial souls who have a purpose and endure over time.",
        "category": "Human Nature"
    },
    {
        "id": 37,
        "question": "According to the text, what are Darwin's three key ideas?",
        "options": [
            "Evolution, creation, and intelligent design",
            "Variation, struggle for existence, and natural selection",
            "Adaptation, mutation, and survival",
            "Competition, cooperation, and extinction"
        ],
        "correct": 1,
        "explanation": "Darwin proposed three key ideas: variation (organisms have different features), struggle for existence (competition for survival), and natural selection (favorable variations are preserved).",
        "category": "Human Nature"
    },
    {
        "id": 38,
        "question": "How does Darwin's theory challenge the Traditional Western view?",
        "options": [
            "It proves that souls don't exist",
            "It suggests humans evolved from other animals rather than being specially designed",
            "It shows that reason is useless",
            "It demonstrates that purpose doesn't exist"
        ],
        "correct": 1,
        "explanation": "Darwin's theory challenges the Traditional view by suggesting humans evolved from nonhuman ancestors rather than being specially created, undermining the idea of unique human purpose and design.",
        "category": "Human Nature"
    },
    {
        "id": 39,
        "question": "According to the text, what does Darwin say about human mental faculties?",
        "options": [
            "They are completely different from animal faculties",
            "There is no fundamental difference between human and higher mammal mental faculties",
            "Only humans have mental faculties",
            "Mental faculties don't actually exist"
        ],
        "correct": 1,
        "explanation": "Darwin argued that there is no fundamental difference between human mental faculties and those of higher mammals - the difference is one of degree, not kind.",
        "category": "Human Nature"
    },
    {
        "id": 40,
        "question": "What does 'natural selection' mean in Darwin's theory?",
        "options": [
            "Humans consciously choose which traits to develop",
            "Nature actively decides which organisms should survive",
            "Favorable variations are preserved and unfavorable ones destroyed through survival pressures",
            "All variations are equally likely to survive"
        ],
        "correct": 2,
        "explanation": "Natural selection means that environmental pressures lead to the preservation of favorable variations and the destruction of unfavorable ones, as described in Darwin's metaphor of daily and hourly scrutinizing.",
        "category": "Human Nature"
    },
    {
        "id": 41,
        "question": "How did Darwin's theory affect views about human purpose?",
        "options": [
            "It strengthened belief in human purpose",
            "It undermined the idea that humans and their parts are designed for a specific purpose",
            "It proved that purpose exists in nature",
            "It had no effect on views about purpose"
        ],
        "correct": 1,
        "explanation": "Darwin's theory undermined the idea that humans and their organs are designed for a purpose, suggesting instead that they developed through accumulation of countless tiny variations.",
        "category": "Human Nature"
    },
    {
        "id": 42,
        "question": "What is the implication of humans sharing common ancestors with other animals?",
        "options": [
            "Humans are exactly the same as other animals",
            "Human abilities, including reason, are more developed versions of abilities other animals have",
            "Other animals are as intelligent as humans",
            "There are no similarities between humans and animals"
        ],
        "correct": 1,
        "explanation": "If humans evolved from nonhuman ancestors, then human abilities like reason are more developed and powerful versions of the same kinds of abilities that other animals have.",
        "category": "Human Nature"
    },
    {
        "id": 43,
        "question": "According to the text, how does evolution explain complex organs like the eye?",
        "options": [
            "They were designed by an intelligent creator",
            "They appeared suddenly through random chance",
            "They developed gradually through many small improvements over time",
            "They cannot be explained by evolution"
        ],
        "correct": 2,
        "explanation": "Darwin argued that complex organs like the eye could develop gradually through many small improvements, each of which provided some advantage for survival.",
        "category": "Human Nature"
    },
    {
        "id": 44,
        "question": "What does the text suggest about the impact of Darwinian ideas?",
        "options": [
            "They were immediately accepted by everyone",
            "They challenged Traditional Western views and continue to influence contemporary philosophy",
            "They had no impact on philosophical thought",
            "They only affected scientific thinking"
        ],
        "correct": 1,
        "explanation": "The text notes that Darwin's ideas challenged Traditional Western views of human nature and continue to influence contemporary philosophers who have written extensively on evolution's implications.",
        "category": "Human Nature"
    },
    {
        "id": 45,
        "question": "According to the passage, why was Darwin's application of evolution to humans particularly disturbing?",
        "options": [
            "Because it suggested humans came from monkeys",
            "Because it implied humans evolved from earlier nonhuman ancestors, challenging human uniqueness",
            "Because it proved God doesn't exist",
            "Because it made humans seem worthless"
        ],
        "correct": 1,
        "explanation": "Darwin's application to humans was disturbing because it implied humans evolved from earlier nonhuman ancestors, directly challenging the idea of human uniqueness and special creation.",
        "category": "Human Nature"
    },
    {
        "id": 46,
        "question": "What does the 'struggle for existence' involve according to Darwin?",
        "options": [
            "Only violent conflict between organisms",
            "Competition for resources, mates, and survival against diseases and predators",
            "Philosophical debates about meaning",
            "Only competition within the same species"
        ],
        "correct": 1,
        "explanation": "The struggle for existence involves broad competition - for food, mates, avoiding predators, surviving diseases, and other environmental challenges that affect survival and reproduction.",
        "category": "Human Nature"
    },
    {
        "id": 47,
        "question": "How does the text describe the relationship between Traditional Western philosophy and Christian thought?",
        "options": [
            "They are completely opposed to each other",
            "Christianity added the concept of humans being made in God's image to Greek rationalism",
            "They have nothing in common",
            "Christianity rejected all Greek philosophical ideas"
        ],
        "correct": 1,
        "explanation": "The text explains that the Judeo-Christian view incorporates Greek rationalism but adds that humans are made in God's image, have free will, and bear moral responsibility.",
        "category": "Human Nature"
    },
    {
        "id": 48,
        "question": "What does variation mean in Darwin's theory?",
        "options": [
            "All organisms are exactly the same",
            "Animals and plants are sometimes born with features different from their parents",
            "Only humans show variation",
            "Variation only occurs in plants"
        ],
        "correct": 1,
        "explanation": "Variation means that organisms are sometimes born with features that differ from those of their parents, which can then be passed on to their offspring.",
        "category": "Human Nature"
    },
    {
        "id": 49,
        "question": "According to the text, what is one major philosophical implication of Darwin's theory?",
        "options": [
            "It proves materialism is false",
            "It supports the view that humans are essentially physical beings rather than souls with bodies",
            "It demonstrates that consciousness doesn't exist",
            "It shows that philosophy is unnecessary"
        ],
        "correct": 1,
        "explanation": "One implication is support for materialistic views of human nature - if we evolved through natural processes, it suggests we are essentially physical beings rather than souls inhabiting bodies.",
        "category": "Human Nature"
    },
    {
        "id": 50,
        "question": "How does the text characterize the ongoing influence of Darwin's ideas?",
        "options": [
            "They are no longer relevant to philosophy",
            "They continue to raise significant philosophical questions about human nature",
            "They have been completely disproven",
            "They only matter for biology"
        ],
        "correct": 1,
        "explanation": "The text notes that numerous leading contemporary philosophers have written about evolution's implications, showing that Darwin's ideas continue to raise significant philosophical issues.",
        "category": "Human Nature"
    },
    {
        "id": 51,
        "question": "What does the text suggest about the relationship between science and philosophy regarding human nature?",
        "options": [
            "Science and philosophy should never interact",
            "Scientific discoveries like evolution can challenge and influence philosophical views",
            "Philosophy is superior to science",
            "Science has no relevance to philosophical questions"
        ],
        "correct": 1,
        "explanation": "The text demonstrates how Darwin's scientific theory significantly challenged and influenced philosophical views about human nature, showing the important interaction between these fields.",
        "category": "Human Nature"
    },
    {
        "id": 52,
        "question": "According to the passage, what makes humans unique in the Traditional Western view?",
        "options": [
            "Their physical strength",
            "Their ability to reason and their possession of an immaterial soul",
            "Their size and appearance",
            "Their geographical location"
        ],
        "correct": 1,
        "explanation": "The Traditional Western view holds that humans are unique because of their rational abilities and possession of an immaterial soul, distinguishing them from other animals.",
        "category": "Human Nature"
    },
    {
        "id": 53,
        "question": "How does Darwin describe natural selection working?",
        "options": [
            "Nature makes conscious decisions about which organisms survive",
            "Environmental pressures preserve helpful traits and eliminate harmful ones",
            "Scientists conduct experiments to determine survival",
            "Animals choose which traits they want to develop"
        ],
        "correct": 1,
        "explanation": "Darwin describes natural selection as environmental pressures that preserve favorable variations while eliminating unfavorable ones, working like a constant scrutinizing process.",
        "category": "Human Nature"
    },
    {
        "id": 54,
        "question": "What does the text suggest about the rate of evolutionary change?",
        "options": [
            "Evolution happens instantly",
            "Evolution occurs over very long periods through gradual accumulation of small changes",
            "Evolution only happened in the past",
            "Evolution is too fast to observe"
        ],
        "correct": 1,
        "explanation": "The text emphasizes that evolution occurs over millions of years through the gradual accumulation of countless small variations, not through sudden dramatic changes.",
        "category": "Human Nature"
    },
    {
        "id": 55,
        "question": "According to the passage, how might evolution explain altruistic behavior?",
        "options": [
            "Altruism proves evolution is false",
            "Helping behaviors may have evolved to aid group survival and can now extend to strangers",
            "Evolution shows altruism is impossible",
            "Only humans are capable of true altruism"
        ],
        "correct": 1,
        "explanation": "The text suggests that helping behaviors evolved to aid group survival, but modern technology and urban environments now allow us to extend help to strangers beyond our genetic relatives.",
        "category": "Human Nature"
    },

    # Logical Reasoning and Arguments (Questions 56-75)
    {
        "id": 56,
        "question": "What are the two main components of an argument?",
        "options": [
            "Facts and opinions",
            "Premises and conclusion",
            "Questions and answers",
            "Problems and solutions"
        ],
        "correct": 1,
        "explanation": "Arguments consist of premises (which provide reasons or evidence) and a conclusion (the statement that the premises are meant to support).",
        "category": "Logic and Arguments"
    },
    {
        "id": 57,
        "question": "A valid argument is one in which:",
        "options": [
            "The premises are true",
            "The conclusion is true",
            "If the premises are true, the conclusion must be true",
            "Everyone agrees with the conclusion"
        ],
        "correct": 2,
        "explanation": "A valid argument has the correct logical form - if the premises were true, the conclusion would have to be true. Validity is about logical structure, not truth of content.",
        "category": "Logic and Arguments"
    },
    {
        "id": 58,
        "question": "A sound argument is:",
        "options": [
            "Any argument that sounds convincing",
            "A valid argument with true premises",
            "An argument everyone accepts",
            "An argument made by an authority"
        ],
        "correct": 1,
        "explanation": "A sound argument is both valid (correct logical form) and has true premises, making it the strongest type of argument.",
        "category": "Logic and Arguments"
    },
    {
        "id": 59,
        "question": "In Socrates' argument about corruption in the Apology, what logical form does he use?",
        "options": [
            "If-then reasoning (conditional logic)",
            "Simple assertion",
            "Appeal to authority",
            "Circular reasoning"
        ],
        "correct": 0,
        "explanation": "Socrates uses if-then reasoning: Either he corrupts intentionally or unintentionally; if intentionally he would harm himself; if unintentionally he should be educated, not punished.",
        "category": "Logic and Arguments"
    },
    {
        "id": 60,
        "question": "What is the 'either-or' connective in logic?",
        "options": [
            "It means both options must be true",
            "It means at least one of the options is true",
            "It means neither option is true",
            "It means exactly one option is true"
        ],
        "correct": 1,
        "explanation": "The 'either-or' connective typically means that at least one of the connected statements is true, though both could be true unless explicitly stated as exclusive.",
        "category": "Logic and Arguments"
    },
    {
        "id": 61,
        "question": "According to the text, what is the principle of charity in argument reconstruction?",
        "options": [
            "Always agree with the person you're analyzing",
            "Reconstruct arguments to make them as strong and reasonable as possible",
            "Give money to philosophers",
            "Never criticize anyone's arguments"
        ],
        "correct": 1,
        "explanation": "The principle of charity requires reconstructing arguments in their strongest, most reasonable form rather than creating weak versions that are easy to defeat.",
        "category": "Logic and Arguments"
    },
    {
        "id": 62,
        "question": "When reconstructing an argument, what should you do about missing premises?",
        "options": [
            "Ignore them completely",
            "Add any premises that would make the argument stronger",
            "Point out that the argument is incomplete",
            "Assume the author didn't think them through"
        ],
        "correct": 1,
        "explanation": "When reconstructing arguments, you should identify and add missing premises that the author likely assumed, to make the argument as complete and strong as possible.",
        "category": "Logic and Arguments"
    },
    {
        "id": 63,
        "question": "What is a 'logical form' of an argument?",
        "options": [
            "How the argument is written on paper",
            "The abstract structure that shows how premises relate to conclusions",
            "Whether the argument is formal or informal",
            "The length of the argument"
        ],
        "correct": 1,
        "explanation": "Logical form refers to the abstract structure of an argument - the pattern that shows how premises are supposed to lead to conclusions, independent of specific content.",
        "category": "Logic and Arguments"
    },
    {
        "id": 64,
        "question": "In the logical form 'If p then q; p; therefore q,' what is this pattern called?",
        "options": [
            "Modus tollens",
            "Modus ponens",
            "Hypothetical syllogism",
            "Disjunctive syllogism"
        ],
        "correct": 1,
        "explanation": "This is modus ponens, a valid argument form: if the conditional 'if p then q' is true, and p is true, then q must be true.",
        "category": "Logic and Arguments"
    },
    {
        "id": 65,
        "question": "What makes an argument invalid?",
        "options": [
            "False premises",
            "A conclusion that could be false even if the premises are true",
            "An unpopular conclusion",
            "Too many premises"
        ],
        "correct": 1,
        "explanation": "An argument is invalid if its logical form allows the premises to be true while the conclusion is false - the premises don't actually support the conclusion.",
        "category": "Logic and Arguments"
    },
    {
        "id": 66,
        "question": "According to the text, why is it important to put arguments in standard form?",
        "options": [
            "To make them look more academic",
            "To clearly identify premises and conclusions for evaluation",
            "To make them longer",
            "To confuse opponents"
        ],
        "correct": 1,
        "explanation": "Standard form helps clearly identify what the premises and conclusion are, making it easier to evaluate whether the argument is valid and whether the premises are true.",
        "category": "Logic and Arguments"
    },
    {
        "id": 67,
        "question": "What is the difference between deductive and inductive arguments?",
        "options": [
            "Deductive arguments are longer than inductive ones",
            "Deductive arguments aim for certainty, inductive for probability",
            "Deductive arguments are always true, inductive are always false",
            "There is no difference"
        ],
        "correct": 1,
        "explanation": "Deductive arguments aim to provide conclusive support (if premises are true, conclusion must be true), while inductive arguments aim to show the conclusion is probably true.",
        "category": "Logic and Arguments"
    },
    {
        "id": 68,
        "question": "In Socrates' prison dialogue, what type of argument structure does he primarily use?",
        "options": [
            "Simple assertions without support",
            "Analogies and conditional reasoning",
            "Appeals to emotion only",
            "Citations of authority figures"
        ],
        "correct": 1,
        "explanation": "Socrates uses analogies (government as parent) and conditional reasoning (if-then structures) to build his arguments about why he shouldn't escape.",
        "category": "Logic and Arguments"
    },
    {
        "id": 69,
        "question": "What does it mean to 'beg the question' in logic?",
        "options": [
            "To ask a lot of questions",
            "To assume what you're trying to prove (circular reasoning)",
            "To ask politely for something",
            "To raise an important issue"
        ],
        "correct": 1,
        "explanation": "Begging the question means assuming in your premises the very thing you're trying to prove in your conclusion, making the argument circular and invalid.",
        "category": "Logic and Arguments"
    },
    {
        "id": 70,
        "question": "According to the text, what should you do when evaluating someone's argument?",
        "options": [
            "Automatically reject it if you disagree",
            "Check both the logical validity and the truth of the premises",
            "Only consider whether you like the conclusion",
            "Accept it if the person seems confident"
        ],
        "correct": 1,
        "explanation": "Proper argument evaluation requires checking both whether the logical form is valid and whether the premises are actually true or at least plausible.",
        "category": "Logic and Arguments"
    },
    {
        "id": 71,
        "question": "What role do assumptions play in arguments?",
        "options": [
            "Assumptions should always be avoided",
            "Unstated assumptions often serve as hidden premises that need to be identified",
            "Assumptions make arguments stronger",
            "Only weak arguments contain assumptions"
        ],
        "correct": 1,
        "explanation": "Many arguments rely on unstated assumptions that function as hidden premises. Identifying these assumptions is crucial for properly understanding and evaluating arguments.",
        "category": "Logic and Arguments"
    },
    {
        "id": 72,
        "question": "In the dialogue format, how does Socrates typically proceed?",
        "options": [
            "By giving long lectures",
            "By asking questions that expose contradictions in his opponent's views",
            "By appealing to religious authority",
            "By using force and intimidation"
        ],
        "correct": 1,
        "explanation": "Socrates uses systematic questioning to reveal contradictions and inconsistencies in people's beliefs, forcing them to examine their assumptions more carefully.",
        "category": "Logic and Arguments"
    },
    {
        "id": 73,
        "question": "What makes Socrates' method of argumentation distinctive?",
        "options": [
            "He never asks questions",
            "He uses questioning to expose ignorance rather than to convey information",
            "He only argues with philosophers",
            "He avoids all logical reasoning"
        ],
        "correct": 1,
        "explanation": "Socrates' distinctive method uses questions not to teach facts but to expose ignorance and false confidence, encouraging genuine inquiry into fundamental questions.",
        "category": "Logic and Arguments"
    },
    {
        "id": 74,
        "question": "According to the text, what is the goal of philosophical argumentation?",
        "options": [
            "To win debates and defeat opponents",
            "To seek truth and understanding through rational inquiry",
            "To show off intellectual superiority",
            "To confuse and intimidate others"
        ],
        "correct": 1,
        "explanation": "The goal of philosophical argumentation is to seek truth and understanding through rational inquiry, not merely to win debates or show intellectual dominance.",
        "category": "Logic and Arguments"
    },
    {
        "id": 75,
        "question": "How should premises and conclusions be related in a good argument?",
        "options": [
            "They should be completely unrelated",
            "The premises should provide good reasons to accept the conclusion",
            "The conclusion should be more interesting than the premises",
            "They should all say the same thing"
        ],
        "correct": 1,
        "explanation": "In a good argument, premises should provide good reasons or evidence that logically support accepting the conclusion.",
        "category": "Logic and Arguments"
    },

    # Applied Philosophy and Ethics (Questions 76-85)
    {
        "id": 76,
        "question": "According to the 'Philosophy and Life' section on civil disobedience, when might breaking the law be justified?",
        "options": [
            "Never, laws should always be obeyed",
            "When one believes the law is unjust and accepts the consequences",
            "Whenever it's convenient",
            "Only when everyone agrees"
        ],
        "correct": 1,
        "explanation": "The text suggests that civil disobedience might be justified when protesting unjust laws, but protesters should be willing to accept legal consequences for their actions.",
        "category": "Applied Ethics"
    },
    {
        "id": 77,
        "question": "How does the text relate Socrates' situation to modern civil disobedience?",
        "options": [
            "They are completely different situations",
            "Both involve individuals choosing conscience over legal compliance",
            "Modern protesters are always wrong",
            "Socrates would have supported all law-breaking"
        ],
        "correct": 1,
        "explanation": "Both situations involve individuals who believe their conscience requires them to act against legal requirements, though they approach the consequences differently.",
        "category": "Applied Ethics"
    },
    {
        "id": 78,
        "question": "What does Albert Ellis's Rational Emotive Behavior Therapy suggest about philosophy's practical value?",
        "options": [
            "Philosophy has no practical applications",
            "Irrational philosophical beliefs can cause psychological problems",
            "Only philosophers can benefit from philosophical thinking",
            "Philosophy makes people more emotional"
        ],
        "correct": 1,
        "explanation": "Ellis argues that irrational philosophical beliefs (like 'I must be perfect' or 'life must be fair') are sources of anxiety, depression, and other psychological problems.",
        "category": "Applied Ethics"
    },
    {
        "id": 79,
        "question": "According to Ellis, what are the three main irrational beliefs that cause problems?",
        "options": [
            "Fear, anger, and sadness",
            "I must do well and get approval, you must treat me reasonably, life must be fair and hassle-free",
            "Work, family, and money concerns",
            "Past, present, and future worries"
        ],
        "correct": 1,
        "explanation": "Ellis identifies three core irrational beliefs: demanding perfection and approval for oneself, demanding reasonable treatment from others, and demanding that life be fair and easy.",
        "category": "Applied Ethics"
    },
    {
        "id": 80,
        "question": "How does philosophical thinking relate to everyday decision-making according to the text?",
        "options": [
            "Philosophy has nothing to do with daily life",
            "Philosophical assumptions underlie our practical choices and worldviews",
            "Only major life decisions involve philosophy",
            "Philosophy makes decision-making impossible"
        ],
        "correct": 1,
        "explanation": "The text argues that our philosophical assumptions about human nature, knowledge, and values deeply influence how we make everyday decisions and understand the world.",
        "category": "Applied Ethics"
    },
    {
        "id": 81,
        "question": "What does the text suggest about the relationship between philosophy and personal freedom?",
        "options": [
            "Philosophy restricts personal freedom",
            "Philosophy helps achieve freedom from unexamined assumptions",
            "Freedom and philosophy are unrelated",
            "Only philosophers can be truly free"
        ],
        "correct": 1,
        "explanation": "The text argues that philosophy helps achieve freedom by liberating us from unexamined assumptions and enabling us to make more autonomous, reasoned decisions.",
        "category": "Applied Ethics"
    },
    {
        "id": 82,
        "question": "How does the text characterize the value of questioning authority?",
        "options": [
            "Authority should never be questioned",
            "Questioning authority is important for intellectual independence and avoiding manipulation",
            "Only political authority should be questioned",
            "Questioning leads to chaos"
        ],
        "correct": 1,
        "explanation": "The text emphasizes that questioning authority and received wisdom is essential for intellectual independence and protection against manipulation by those seeking to influence our thinking.",
        "category": "Applied Ethics"
    },
    {
        "id": 83,
        "question": "What does Voltaire's story of the Brahmin illustrate about philosophy?",
        "options": [
            "Ignorance is always better than knowledge",
            "There can be tension between philosophical wisdom and simple happiness",
            "Philosophy guarantees happiness",
            "Only religious people can be happy"
        ],
        "correct": 1,
        "explanation": "The Brahmin story illustrates the potential tension between philosophical wisdom (which brings awareness of complexity and uncertainty) and simple, unreflective happiness.",
        "category": "Applied Ethics"
    },
    {
        "id": 84,
        "question": "According to the text, how should we approach conflicting philosophical viewpoints?",
        "options": [
            "Always choose the most popular view",
            "Examine them carefully using critical thinking and evidence",
            "Avoid philosophy altogether",
            "Accept whatever authorities tell us"
        ],
        "correct": 1,
        "explanation": "The text advocates using critical thinking skills to carefully examine conflicting viewpoints, evaluating evidence and reasoning rather than simply accepting popular or authoritative positions.",
        "category": "Applied Ethics"
    },
    {
        "id": 85,
        "question": "What is the ultimate message about philosophy's role in human life according to this text?",
        "options": [
            "Philosophy is only for academic specialists",
            "Philosophy is an essential tool for examined living and human flourishing",
            "Philosophy always leads to unhappiness",
            "Philosophy should be avoided by practical people"
        ],
        "correct": 1,
        "explanation": "The text presents philosophy as essential for the examined life - helping us think critically, question assumptions, achieve freedom from unexamined beliefs, and live more autonomous, thoughtful lives.",
        "category": "Applied Ethics"
    }
]

def display_quiz():
    st.title("📚 Week 4: Philosophy Quiz")
    st.markdown("## Comprehensive Assessment - 85 Questions")
    st.markdown("*Based on Ancient Philosophy, Human Nature, Darwin's Challenge, and Socratic Method*")
    
    total_questions = len(QUIZ_QUESTIONS)
    answered_count = len(st.session_state.answers)
    
    # Progress bar and stats
    progress = answered_count / total_questions
    st.progress(progress)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Progress", f"{answered_count}/{total_questions}")
    with col2:
        st.metric("Percentage", f"{progress:.1%}")
    with col3:
        if answered_count > 0:
            correct_count = sum(1 for ans in st.session_state.answers.values() 
                              if ans['selected'] == ans['correct'])
            current_score = correct_count / answered_count
            st.metric("Current Score", f"{current_score:.1%}")
    
    if not st.session_state.quiz_completed:
        current_q_index = st.session_state.current_question
        question = QUIZ_QUESTIONS[current_q_index]
        
        st.markdown("---")
        st.markdown(f"### Question {current_q_index + 1} of {total_questions}")
        st.markdown(f"**Category:** {question['category']}")
        
        # Display feedback if question was already answered
        if question['id'] in st.session_state.answers:
            prev_answer = st.session_state.answers[question['id']]
            selected_option = question['options'][prev_answer['selected']]
            correct_option = question['options'][prev_answer['correct']]
            
            if prev_answer['selected'] == prev_answer['correct']:
                st.success(f"✅ **Correct!** You selected: {selected_option}")
            else:
                st.error(f"❌ **Incorrect.** You selected: {selected_option}")
                st.info(f"**Correct answer:** {correct_option}")
            
            st.info(f"**Explanation:** {question['explanation']}")
            st.markdown("---")

        # Question display
        st.markdown(f"**{question['question']}**")
        
        # Get current selection
        if question['id'] in st.session_state.answers:
            default_index = st.session_state.answers[question['id']]['selected']
        else:
            default_index = 0
            
        selected_answer = st.radio(
            "Choose your answer:",
            options=question['options'],
            index=default_index,
            key=f"question_{question['id']}"
        )
        
        def store_current_answer():
            selected_index = question['options'].index(selected_answer)
            st.session_state.answers[question['id']] = {
                'selected': selected_index,
                'correct': question['correct'],
                'category': question['category']
            }

        # Navigation buttons
        st.markdown("---")
        nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1, 1, 1, 1])
        
        with nav_col1:
            if st.button("⬅️ Previous", disabled=(current_q_index <= 0)):
                store_current_answer()
                st.session_state.current_question -= 1
                st.rerun()
                
        with nav_col2:
            if current_q_index < total_questions - 1:
                if st.button("Next ➡️"):
                    store_current_answer()
                    st.session_state.current_question += 1
                    st.rerun()
                    
        with nav_col3:
            # Jump to question
            jump_to = st.selectbox("Jump to:", range(1, total_questions + 1), 
                                 value=current_q_index + 1, key="jump_select")
            if st.button("Go"):
                store_current_answer()
                st.session_state.current_question = jump_to - 1
                st.rerun()

        with nav_col4:
            if answered_count >= total_questions:
                if st.button("🏁 Finish Quiz", type="primary"):
                    store_current_answer()
                    st.session_state.quiz_completed = True
                    st.rerun()
            else:
                st.write(f"Answer {total_questions - answered_count} more questions to finish")

    else:
        # Results display
        st.balloons()
        st.header("🎉 Quiz Complete!")
        
        # Calculate scores
        total_correct = 0
        category_stats = {}
        
        for q in QUIZ_QUESTIONS:
            category = q['category']
            if category not in category_stats:
                category_stats[category] = {'correct': 0, 'total': 0}
            
            category_stats[category]['total'] += 1
            
            if q['id'] in st.session_state.answers:
                answer = st.session_state.answers[q['id']]
                if answer['selected'] == answer['correct']:
                    total_correct += 1
                    category_stats[category]['correct'] += 1
        
        overall_percentage = (total_correct / total_questions) * 100
        
        # Overall results
        st.success(f"**Final Score: {total_correct}/{total_questions} ({overall_percentage:.1f}%)**")
        
        # Grade
        if overall_percentage >= 90:
            grade = "A"
            st.success("🏆 Excellent work!")
        elif overall_percentage >= 80:
            grade = "B" 
            st.info("👍 Good job!")
        elif overall_percentage >= 70:
            grade = "C"
            st.warning("📚 Consider reviewing the material")
        elif overall_percentage >= 60:
            grade = "D"
            st.warning("📖 More study needed")
        else:
            grade = "F"
            st.error("📚 Please review the material thoroughly")
            
        st.markdown(f"**Grade: {grade}**")
        
        # Category breakdown
        st.markdown("### Performance by Category:")
        for category, stats in category_stats.items():
            if stats['total'] > 0:
                cat_percentage = (stats['correct'] / stats['total']) * 100
                st.markdown(f"**{category}:** {stats['correct']}/{stats['total']} ({cat_percentage:.1f}%)")
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Retake Quiz", type="primary"):
                st.session_state.current_question = 0
                st.session_state.answers = {}
                st.session_state.quiz_completed = False
                st.rerun()
                
        with col2:
            if st.button("📊 Review Answers"):
                st.session_state.quiz_completed = False
                st.session_state.current_question = 0
                st.rerun()

# Run the quiz
display_quiz()
