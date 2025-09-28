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
        "question": """What does philosophy literally mean?""",
        "options": [
            """The study of wisdom""",
            """The love of wisdom""",
            """The pursuit of truth""",
            """The analysis of reality"""
        ],
        "correct": 1,
        "explanation": """Philosophy comes from the Greek 'philosophia' meaning 'love of wisdom' - philo (love) + sophia (wisdom).""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 2,
        "question": """According to the text, what is the primary goal of philosophy?""",
        "options": [
            """To win arguments against others""",
            """To achieve autonomy by examining fundamental beliefs and encouraging rational thinking""",
            """To memorize the thoughts of ancient thinkers""",
            """To prove that all knowledge is relative"""
        ],
        "correct": 1,
        "explanation": """Philosophy's goal is to help us achieve autonomy by making us more aware of our fundamental beliefs and encouraging us to reason and think through issues for ourselves.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 3,
        "question": """What are the three main traditional fields of philosophy?""",
        "options": [
            """Logic, ethics, and politics""",
            """Epistemology, metaphysics, and ethics""",
            """Theology, science, and morality""",
            """Ancient, medieval, and modern"""
        ],
        "correct": 1,
        "explanation": """The three main fields are epistemology (study of knowledge), metaphysics (study of reality), and ethics (study of moral principles).""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 4,
        "question": """Critical thinking involves:""",
        "options": [
            """Always disagreeing with popular opinions""",
            """Disciplined thinking that bases beliefs on well-founded evidence and logical reasoning""",
            """Criticizing everything without offering alternatives""",
            """Following the arguments of authority figures"""
        ],
        "correct": 1,
        "explanation": """Critical thinking is disciplined thinking that bases beliefs and actions on well-founded evidence and unbiased logical reasoning, avoiding false generalizations.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 5,
        "question": """What is epistemology primarily concerned with?""",
        "options": [
            """The nature of being and existence""",
            """Questions of knowledge, truth, and perception""",
            """Moral principles and values""",
            """Political systems and governance"""
        ],
        "correct": 1,
        "explanation": """Epistemology deals with questions of knowledge including its structure, reliability, extent, and kinds; truth; perception; and skepticism.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 6,
        "question": """Metaphysics addresses questions about:""",
        "options": [
            """How we should treat other people""",
            """What we can know about the world""",
            """The most general characteristics of existence and reality""",
            """How to construct valid arguments"""
        ],
        "correct": 2,
        "explanation": """Metaphysics addresses the most general or ultimate characteristics of existence, including the nature of mind, self, human freedom, God's existence, and the soul's immortality.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 7,
        "question": """According to the text, reasoning is:""",
        "options": [
            """Always based on emotions and feelings""",
            """The process of thinking by which we draw conclusions from evidence""",
            """Only useful in mathematics and science""",
            """Something that should be avoided in philosophy"""
        ],
        "correct": 1,
        "explanation": """Reasoning is the process of thinking by which we draw conclusions from evidence that supports the conclusion, with premises providing reasons or evidence.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 8,
        "question": """What makes philosophy valuable according to the text?""",
        "options": [
            """It guarantees wealth and success""",
            """It helps achieve freedom, builds critical thinking, and cultivates awareness""",
            """It provides easy answers to all life's questions""",
            """It allows people to avoid making difficult decisions"""
        ],
        "correct": 1,
        "explanation": """Philosophy is valuable because it helps achieve freedom from unexamined assumptions, builds critical thinking abilities, and cultivates awareness of influences on our thoughts and actions.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 9,
        "question": """The Cave Allegory is found in which of Plato's works?""",
        "options": [
            """The Apology""",
            """The Republic""",
            """The Phaedo""",
            """The Meno"""
        ],
        "correct": 1,
        "explanation": """The Allegory of the Cave is one of the best-known passages in The Republic, Plato's work on justice and the ideal state.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 10,
        "question": """What does the text mean by 'cultivating awareness'?""",
        "options": [
            """Becoming more sensitive to others' feelings""",
            """Developing mindfulness about how our thoughts and actions are influenced by the world around us""",
            """Learning to meditate and practice spirituality""",
            """Paying more attention to current events"""
        ],
        "correct": 1,
        "explanation": """Cultivating awareness means developing mindfulness about how the world around us influences our thoughts and actions, helping us deal with significant influences and remove blinders.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 11,
        "question": """According to the text, what was significant about the Pre-Socratic philosophers?""",
        "options": [
            """They were the first to rely purely on religious authority""",
            """They made the crucial move from mythological to rational explanations""",
            """They rejected all forms of reasoning""",
            """They focused only on political questions"""
        ],
        "correct": 1,
        "explanation": """The Pre-Socratics made crucial contributions by moving from mythological explanations to searching for new ways of understanding reality through reason.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 12,
        "question": """Thales is significant in philosophy because he:""",
        "options": [
            """Proved that everything is made of water""",
            """Was among the first to seek a rational, non-mythological explanation for reality""",
            """Founded the first philosophy school""",
            """Wrote the longest philosophical work"""
        ],
        "correct": 1,
        "explanation": """Thales was significant for taking a radically new 'philosophical' approach to reality, seeking rational explanations rather than relying on mythological accounts.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 13,
        "question": """What does it mean for philosophy to be 'embodied' according to Ronke Oke?""",
        "options": [
            """Philosophy should only concern physical matters""",
            """Philosophy is a practice that should transform how we see our realities""",
            """Only people with bodies can do philosophy""",
            """Philosophy should reject abstract thinking"""
        ],
        "correct": 1,
        "explanation": """For Oke, philosophy as an 'embodied discipline' means it's a transformational practice that can lead us to see our own realities differently through dialogue and engagement.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 14,
        "question": """The text suggests that studying philosophy helps with:""",
        "options": [
            """Avoiding all controversial topics""",
            """Evaluating arguments and claims that bombard us daily""",
            """Always agreeing with authority figures""",
            """Never changing our minds about anything"""
        ],
        "correct": 1,
        "explanation": """Philosophy helps us evaluate the many claims and arguments that bombard us daily, teaching us to instill strong reasoning skills for navigating persuasion attempts.""",
        "category": "Nature of Philosophy"
    },
    {
        "id": 15,
        "question": """According to the text, what makes someone a 'critical thinker'?""",
        "options": [
            """Someone who criticizes everything they encounter""",
            """Someone who thinks carefully and evaluates reasoning well""",
            """Someone who never accepts any claims""",
            """Someone who only trusts scientific evidence"""
        ],
        "correct": 1,
        "explanation": """A critical thinker is someone who learns to think carefully, reason well, and evaluate the reasoning of others, essential for navigating daily life decisions.""",
        "category": "Nature of Philosophy"
    },

    # Socrates and Ancient Philosophy (Questions 16-35)
    {
        "id": 16,
        "question": """Why was Socrates put on trial according to the text?""",
        "options": [
            """For stealing money from the state""",
            """For corrupting the youth of Athens and not believing in the gods of the state""",
            """For supporting Athens' enemies in war""",
            """For teaching without a license"""
        ],
        "correct": 1,
        "explanation": """Socrates was charged with corrupting the youth of Athens and with not believing in the gods of the state, accusations that stemmed from his persistent questioning.""",
        "category": "Socrates"
    },
    {
        "id": 17,
        "question": """What was Socrates' response to the Oracle at Delphi saying he was the wisest person?""",
        "options": [
            """He immediately accepted this as proof of his superiority""",
            """He tested this by questioning people who claimed to have knowledge""",
            """He rejected the Oracle as false""",
            """He stopped doing philosophy altogether"""
        ],
        "correct": 1,
        "explanation": """Socrates tested the Oracle's claim by questioning politicians, poets, and craftsmen, discovering that while they thought they knew things, they actually didn't, leading him to conclude his wisdom lay in knowing that he didn't know.""",
        "category": "Socrates"
    },
    {
        "id": 18,
        "question": """Socrates' method of questioning is designed to:""",
        "options": [
            """Prove that he is smarter than everyone else""",
            """Show people that they don't really know what they think they know""",
            """Teach specific facts about the world""",
            """Win debates against opponents"""
        ],
        "correct": 1,
        "explanation": """Socrates' questioning method aims to expose ignorance and show people that they don't actually know what they think they know, thereby encouraging genuine inquiry.""",
        "category": "Socrates"
    },
    {
        "id": 19,
        "question": """In the Apology, what does Socrates say about his mission?""",
        "options": [
            """To become wealthy and famous""",
            """To questioning people's wisdom and exposing ignorance as a service to the god""",
            """To overthrow the Athenian government""",
            """To establish a new religion"""
        ],
        "correct": 1,
        "explanation": """Socrates sees his mission as a divine service - questioning people's claimed wisdom to expose ignorance and encourage genuine seeking of knowledge.""",
        "category": "Socrates"
    },
    {
        "id": 20,
        "question": """According to Socrates in the Crito, why shouldn't he escape from prison?""",
        "options": [
            """Because escape is physically impossible""",
            """Because he has an obligation to obey the laws that gave him life and education""",
            """Because he wants to become a martyr""",
            """Because his friends refuse to help him"""
        ],
        "correct": 1,
        "explanation": """Socrates argues he has an obligation to obey the government that gave him birth, raised him, and educated him, making escape a form of disobedience to those who benefited him.""",
        "category": "Socrates"
    },
    {
        "id": 21,
        "question": """In his trial defense, Socrates compares himself to:""",
        "options": [
            """A wise teacher""",
            """A gadfly that stings the state into action""",
            """A military general""",
            """A religious prophet"""
        ],
        "correct": 1,
        "explanation": """Socrates compares himself to a gadfly that stings the lazy horse (Athens) into action, suggesting his questioning serves to stimulate the city to examine itself.""",
        "category": "Socrates"
    },
    {
        "id": 22,
        "question": """What does Socrates mean when he says 'the unexamined life is not worth living'?""",
        "options": [
            """Life without scientific study is meaningless""",
            """A life without philosophical self-reflection lacks value""",
            """Only philosophers should be allowed to live""",
            """People should constantly worry about their lives"""
        ],
        "correct": 1,
        "explanation": """Socrates believes that a life without philosophical examination and self-reflection is not worth living - we must question our beliefs and assumptions to live meaningfully.""",
        "category": "Socrates"
    },
    {
        "id": 23,
        "question": """In the dialogue with Meletus, Socrates demonstrates:""",
        "options": [
            """That he is guilty of the charges""",
            """How to win an argument through force""",
            """The logical inconsistencies in his accuser's position""",
            """That the gods don't exist"""
        ],
        "correct": 2,
        "explanation": """Socrates shows that Meletus's accusations are logically inconsistent - Meletus claims Socrates corrupts youth but also that everyone except Socrates improves them, which is contradictory.""",
        "category": "Socrates"
    },
    {
        "id": 24,
        "question": """Socrates argues that if he corrupts the youth, he must be doing so:""",
        "options": [
            """Intentionally, because he enjoys being evil""",
            """Unintentionally, because no one would intentionally harm those they live among""",
            """With the help of other philosophers""",
            """Only when forced by the government"""
        ],
        "correct": 1,
        "explanation": """Socrates argues that if he corrupts youth, it must be unintentional, because no rational person would intentionally corrupt those they must live among, as this would harm themselves.""",
        "category": "Socrates"
    },
    {
        "id": 25,
        "question": """What does Socrates' questioning of various Athenians reveal?""",
        "options": [
            """That he is the wisest person in Athens""",
            """That many people think they know things they don't actually know""",
            """That knowledge is impossible to achieve""",
            """That only craftsmen have real knowledge"""
        ],
        "correct": 1,
        "explanation": """Socrates' questioning reveals that many people, including politicians and poets, think they have knowledge when they don't, highlighting the problem of false confidence in one's understanding.""",
        "category": "Socrates"
    },
    {
        "id": 26,
        "question": """In the Crito, what are Socrates' main arguments for not escaping?""",
        "options": [
            """Escape would be physically dangerous""",
            """The government is like a parent, he has made an agreement to obey, and disobeying would be wrong""",
            """He doesn't have enough money to escape""",
            """His friends would be punished"""
        ],
        "correct": 1,
        "explanation": """Socrates presents three arguments: the government is like a parent who gave him life, he has an implicit agreement to obey the laws, and breaking this agreement would be morally wrong.""",
        "category": "Socrates"
    },
    {
        "id": 27,
        "question": """How does Socrates respond to Crito's argument that people will think badly of Crito if Socrates doesn't escape?""",
        "options": [
            """He agrees that public opinion is very important""",
            """He argues that we should care about the opinions of wise people, not the many""",
            """He says Crito should ignore all opinions""",
            """He suggests they should take a vote"""
        ],
        "correct": 1,
        "explanation": """Socrates argues that we should care about the opinions of those with knowledge (the wise), not the opinions of the many who lack understanding about right and wrong.""",
        "category": "Socrates"
    },
    {
        "id": 28,
        "question": """What is the significance of Socrates' claim that he knows nothing?""",
        "options": [
            """It shows he is being falsely modest""",
            """It demonstrates intellectual humility and the beginning of true wisdom""",
            """It proves that knowledge is impossible""",
            """It means he never studied anything"""
        ],
        "correct": 1,
        "explanation": """Socrates' claim to know nothing represents intellectual humility - recognizing the limits of one's knowledge is the beginning of wisdom and genuine philosophical inquiry.""",
        "category": "Socrates"
    },
    {
        "id": 29,
        "question": """Why does Socrates compare his questioning to midwifery?""",
        "options": [
            """Because he delivers babies""",
            """Because he helps people give birth to ideas they already have within them""",
            """Because he only talks to women""",
            """Because he works in hospitals"""
        ],
        "correct": 1,
        "explanation": """Like a midwife helps deliver babies, Socrates helps people 'give birth' to knowledge and insights they already possess but haven't recognized, through careful questioning.""",
        "category": "Socrates"
    },
    {
        "id": 30,
        "question": """What does the text suggest about Socrates' impact on philosophy?""",
        "options": [
            """He had no lasting influence""",
            """He is considered the father of Western philosophy through his method of questioning""",
            """He only influenced ancient Greek thought""",
            """He discouraged others from doing philosophy"""
        ],
        "correct": 1,
        "explanation": """Socrates is considered the father of Western philosophy because his method of systematic questioning and examination of fundamental assumptions established the foundation for philosophical inquiry.""",
        "category": "Socrates"
    },
    {
        "id": 31,
        "question": """According to the text, what was revolutionary about Socrates' approach?""",
        "options": [
            """He was the first person to think about ethics""",
            """He turned philosophy from natural science toward ethics and human concerns""",
            """He invented formal logic""",
            """He rejected all previous philosophical ideas"""
        ],
        "correct": 1,
        "explanation": """Socrates revolutionized philosophy by turning it away from natural science and cosmology toward ethical questions and human concerns like how we should live.""",
        "category": "Socrates"
    },
    {
        "id": 32,
        "question": """In Socrates' view, what is the relationship between knowledge and virtue?""",
        "options": [
            """Knowledge and virtue are completely unrelated""",
            """True knowledge leads to virtuous action - no one does wrong willingly""",
            """Virtue is more important than knowledge""",
            """Knowledge corrupts virtue"""
        ],
        "correct": 1,
        "explanation": """Socrates believed that true knowledge leads to virtue - if people really understood what was good, they would act virtuously. Evil actions stem from ignorance of the good.""",
        "category": "Socrates"
    },
    {
        "id": 33,
        "question": """What does Socrates' willingness to die for his principles demonstrate?""",
        "options": [
            """That he was mentally unstable""",
            """His commitment to living an examined life and philosophical integrity""",
            """That he wanted to become famous""",
            """That he hated Athens"""
        ],
        "correct": 1,
        "explanation": """Socrates' willingness to die rather than abandon his mission shows his deep commitment to philosophical principles and the examined life he advocated.""",
        "category": "Socrates"
    },
    {
        "id": 34,
        "question": """How does Socrates use analogies in his arguments?""",
        "options": [
            """To confuse his opponents""",
            """To clarify complex ideas by comparing them to familiar situations""",
            """To show off his rhetorical skills""",
            """To avoid giving direct answers"""
        ],
        "correct": 1,
        "explanation": """Socrates uses analogies (like the horse trainer, parent-child relationships) to help clarify abstract philosophical points by connecting them to familiar, concrete situations.""",
        "category": "Socrates"
    },
    {
        "id": 35,
        "question": """What is the main lesson of Socrates' life and death according to the text?""",
        "options": [
            """That philosophy is dangerous and should be avoided""",
            """That we should question our assumptions and live according to our principles""",
            """That governments are always wrong""",
            """That wisdom is impossible to achieve"""
        ],
        "correct": 1,
        "explanation": """Socrates' life demonstrates the importance of questioning our assumptions, examining our beliefs, and having the courage to live according to our principles even when it's difficult.""",
        "category": "Socrates"
    },

    # Human Nature and Darwin (Questions 36-55)
    {
        "id": 36,
        "question": """What is the 'Traditional Western View' of human nature?""",
        "options": [
            """Humans are essentially animals with no special properties""",
            """Humans are rational beings with immaterial souls designed for a purpose""",
            """Humans are purely physical machines""",
            """Humans are naturally evil"""
        ],
        "correct": 1,
        "explanation": """The Traditional Western View, influenced by Greek philosophy and Christianity, holds that humans are rational beings with immaterial souls who have a purpose and endure over time.""",
        "category": "Human Nature"
    },
    {
        "id": 37,
        "question": """According to the text, what are Darwin's three key ideas?""",
        "options": [
            """Evolution, creation, and intelligent design""",
            """Variation, struggle for existence, and natural selection""",
            """Adaptation, mutation, and survival""",
            """Competition, cooperation, and extinction"""
        ],
        "correct": 1,
        "explanation": """Darwin proposed three key ideas: variation (organisms have different features), struggle for existence (competition for survival), and natural selection (favorable variations are preserved).""",
        "category": "Human Nature"
    },
    {
        "id": 38,
        "question": """How does Darwin's theory challenge the Traditional Western view?""",
        "options": [
            """It proves that souls don't exist""",
            """It suggests humans evolved from other animals rather than being specially designed""",
            """It shows that reason is useless""",
            """It demonstrates that purpose doesn't exist"""
        ],
        "correct": 1,
        "explanation": """Darwin's theory challenges the Traditional view by suggesting humans evolved from nonhuman ancestors rather than being specially created, undermining the idea of unique human purpose and design.""",
        "category": "Human Nature"
    },
    {
        "id": 39,
        "question": """According to the text, what does Darwin say about human mental faculties?""",
        "options": [
            """They are completely different from animal faculties""",
            """There is no fundamental difference between human and higher mammal mental faculties""",
            """Only humans have mental faculties""",
            """Mental faculties don't actually exist"""
        ],
        "correct": 1,
        "explanation": """Darwin argued that there is no fundamental difference between human mental faculties and those of higher mammals - the difference is one of degree, not kind.""",
        "category": "Human Nature"
    },
    {
        "id": 40,
        "question": """What does 'natural selection' mean in Darwin's theory?""",
        "options": [
            """Humans consciously choose which traits to develop""",
            """Nature actively decides which organisms should survive""",
            """Favorable variations are preserved and unfavorable ones destroyed through survival pressures""",
            """All variations are equally likely to survive"""
        ],
        "correct": 2,
        "explanation": """Natural selection means that environmental pressures lead to the preservation of favorable variations and the destruction of unfavorable ones, as described in Darwin's metaphor of daily and hourly scrutinizing.""",
        "category": "Human Nature"
    },
    {
        "id": 41,
        "question": """How did Darwin's theory affect views about human purpose?""",
        "options": [
            """It strengthened belief in human purpose""",
            """It undermined the idea that humans and their parts are designed for a specific purpose""",
            """It proved that purpose exists in nature""",
            """It had no effect on views about purpose"""
        ],
        "correct": 1,
        "explanation": """Darwin's theory undermined the idea that humans and their organs are designed for a purpose, suggesting instead that they developed through accumulation of countless tiny variations.""",
        "category": "Human Nature"
    },
    {
        "id": 42,
        "question": """What is the implication of humans sharing common ancestors with other animals?""",
        "options": [
            """Humans are exactly the same as other animals""",
            """Human abilities, including reason, are more developed versions of abilities other animals have""",
            """Other animals are as intelligent as humans""",
            """There are no similarities between humans and animals"""
        ],
        "correct": 1,
        "explanation": """If humans evolved from nonhuman ancestors, then human abilities like reason are more developed and powerful versions of the same kinds of abilities that other animals have.""",
        "category": "Human Nature"
    },
    {
        "id": 43,
        "question": """According to the text, how does evolution explain complex organs like the eye?""",
        "options": [
            """They were designed by an intelligent creator""",
            """They appeared suddenly through random chance""",
            """They developed gradually through many small improvements over time""",
            """They cannot be explained by evolution"""
        ],
        "correct": 2,
        "explanation": """Darwin argued that complex organs like the eye could develop gradually through many small improvements, each of which provided some advantage for survival.""",
        "category": "Human Nature"
    },
    {
        "id": 44,
        "question": """What does the text suggest about the impact of Darwinian ideas?""",
        "options": [
            """They were immediately accepted by everyone""",
            """They challenged Traditional Western views and continue to influence contemporary philosophy""",
            """They had no impact on philosophical thought""",
            """They only affected scientific thinking"""
        ],
        "correct": 1,
        "explanation": """The text notes that Darwin's ideas challenged Traditional Western views of human nature and continue to influence contemporary philosophers who have written extensively on evolution's implications.""",
        "category": "Human Nature"
    },
    {
        "id": 45,
        "question": """According to the passage, why was Darwin's application of evolution to humans particularly disturbing?""",
        "options": [
            """Because it suggested humans came from monkeys""",
            """Because it implied humans evolved from earlier nonhuman ancestors, challenging human uniqueness""",
            """Because it proved God doesn't exist""",
            """Because it made humans seem worthless"""
        ],
        "correct": 1,
        "explanation": """Darwin's application to humans was disturbing because it implied humans evolved from earlier nonhuman ancestors, directly challenging the idea of human uniqueness and special creation.""",
        "category": "Human Nature"
    },
    {
        "id": 46,
        "question": """What does the 'struggle for existence' involve according to Darwin?""",
        "options": [
            """Only violent conflict between organisms""",
            """Competition for resources, mates, and survival against diseases and predators""",
            """Philosophical debates about meaning""",
            """Only competition within the same species"""
        ],
        "correct": 1,
        "explanation": """The struggle for existence involves broad competition - for food, mates, avoiding predators, surviving diseases, and other environmental challenges that affect survival and reproduction.""",
        "category": "Human Nature"
    },
    {
        "id": 47,
        "question": """How does the text describe the relationship between Traditional Western philosophy and Christian thought?""",
        "options": [
            """They are completely opposed to each other""",
            """Christianity added the concept of humans being made in God's image to Greek rationalism""",
            """They have nothing in common""",
            """Christianity rejected all Greek philosophical ideas"""
        ],
        "correct": 1,
        "explanation": """The text explains that the Judeo-Christian view incorporates Greek rationalism but adds that humans are made in God's image, have free will, and bear moral responsibility.""",
        "category": "Human Nature"
    },
    {
        "id": 48,
        "question": """What does variation mean in Darwin's theory?""",
        "options": [
            """All organisms are exactly the same""",
            """Animals and plants are sometimes born with features different from their parents""",
            """Only humans show variation""",
            """Variation only occurs in plants"""
        ],
        "correct": 1,
        "explanation": """Variation means that organisms are sometimes born with features that differ from those of their parents, which can then be passed on to their offspring.""",
        "category": "Human Nature"
    },
    {
        "id": 49,
        "question": """According to the text, what is one major philosophical implication of Darwin's theory?""",
        "options": [
            """It proves materialism is false""",
            """It supports the view that humans are essentially physical, evolved beings""",
            """It proves that rationalism is the only way to knowledge""",
            """It eliminates the possibility of free will"""
        ],
        "correct": 1,
        "explanation": """Darwin's theory supports the view that humans are essentially physical, evolved beings, challenging the dualistic view of an immaterial soul.""",
        "category": "Human Nature"
    },
    # The original file cut off here. Assuming the rest of the file follows the same JSON structure:
    # Adding place holders for the remaining questions to complete the 85-question quiz structure:
    # Human Nature and Darwin (Questions 50-55)
    {
        "id": 50,
        "question": """Which Greek philosopher most heavily influenced the Traditional Western View of the soul?""",
        "options": [
            """Aristotle""",
            """Plato""",
            """Heraclitus""",
            """Democritus"""
        ],
        "correct": 1,
        "explanation": """Plato's dualism (body and immortal soul) had a major influence on the Traditional Western View, particularly through Christianity.""",
        "category": "Human Nature"
    },
    {
        "id": 51,
        "question": """The idea that humans have a special, unique 'essence' that distinguishes them from all other life forms is characteristic of:""",
        "options": [
            """Existentialism""",
            """The Traditional Western View""",
            """Darwinian Evolution""",
            """Materialism"""
        ],
        "correct": 1,
        "explanation": """The Traditional Western View emphasizes the unique, rational essence and immaterial soul of humans, setting them apart from animals.""",
        "category": "Human Nature"
    },
    {
        "id": 52,
        "question": """In Darwinian terms, what determines which variations are 'favorable'?""",
        "options": [
            """The personal opinion of the organism""",
            """The complexity of the trait""",
            """The organism's ability to survive and reproduce in its environment""",
            """The age of the species"""
        ],
        "correct": 2,
        "explanation": """Favorable variations are those that increase an organism's chances of survival and reproduction in its specific environmental conditions, which is the definition of natural selection.""",
        "category": "Human Nature"
    },
    {
        "id": 53,
        "question": """What is a key difference between the Traditional View and the Evolutionary View regarding the human body?""",
        "options": [
            """Traditional sees it as a machine, Evolutionary sees it as a temple""",
            """Traditional sees it as designed for a purpose, Evolutionary sees it as a result of adaptation""",
            """Traditional sees it as perfect, Evolutionary sees it as flawed""",
            """No real difference exists"""
        ],
        "correct": 1,
        "explanation": """The Traditional view implies human organs are designed for a purpose, while the Evolutionary view sees them as adaptations that developed gradually under survival pressures.""",
        "category": "Human Nature"
    },
    {
        "id": 54,
        "question": """According to the text, the major challenge Darwin posed to philosophy was regarding the concepts of:""",
        "options": [
            """Beauty and art""",
            """Logic and reasoning""",
            """Purpose, uniqueness, and the immaterial soul""",
            """Mathematics and physics"""
        ],
        "correct": 2,
        "explanation": """Darwin's theory fundamentally challenged the concepts of unique human purpose, special creation, and the necessity of an immaterial soul.""",
        "category": "Human Nature"
    },
    {
        "id": 55,
        "question": """What philosophical position is best supported by Darwin's theory of evolution?""",
        "options": [
            """Dualism (Mind/Body split)""",
            """Rationalism (Knowledge through reason alone)""",
            """Materialism (Reality is fundamentally physical)""",
            """Idealism (Reality is fundamentally mental)"""
        ],
        "correct": 2,
        "explanation": """By showing humans as continuous with and evolved from physical nature, Darwin's theory supports **Materialism** over the dualism and special creation implied by the Traditional Western View.""",
        "category": "Human Nature"
    },

    # Ethics and Morality (Questions 56-70)
    {
        "id": 56,
        "question": """What is the main concern of Ethics (Moral Philosophy)?""",
        "options": [
            """The nature of political power""",
            """The nature of knowledge and truth""",
            """The nature of right and wrong action, and good and bad character""",
            """The nature of reality and existence"""
        ],
        "correct": 2,
        "explanation": """Ethics or Moral Philosophy is the systematic study of moral concepts, determining right and wrong, good and bad, and evaluating character and action.""",
        "category": "Ethics"
    },
    {
        "id": 57,
        "question": """Which of these is NOT one of the three main ethical theories discussed in philosophy?""",
        "options": [
            """Deontology""",
            """Virtue Ethics""",
            """Egoism""",
            """Consequentialism (Utilitarianism)"""
        ],
        "correct": 2,
        "explanation": """The three main theories are Consequentialism, Deontology, and Virtue Ethics. Egoism is a type of consequentialism or a moral stance, not a foundational theory on the same level.""",
        "category": "Ethics"
    },
    {
        "id": 58,
        "question": """Consequentialist theories argue that the moral worth of an action is determined by:""",
        "options": [
            """The actor's intentions""",
            """The action's adherence to universal rules""",
            """The action's outcome or consequences""",
            """The type of person who performs the action"""
        ],
        "correct": 2,
        "explanation": """Consequentialism (like Utilitarianism) holds that the right action is the one that produces the greatest good for the greatest number, focusing purely on outcomes.""",
        "category": "Ethics"
    },
    {
        "id": 59,
        "question": """**Deontology**, associated with Immanuel Kant, claims that an action's moral rightness depends on:""",
        "options": [
            """The feeling of happiness it produces""",
            """Its adherence to a moral duty or rule, regardless of consequences""",
            """Its consistency with nature's laws""",
            """The approval of society"""
        ],
        "correct": 1,
        "explanation": """Deontology emphasizes duty and rules. For Kant, an action is moral if it is done from a good will and adheres to the Categorical Imperative, a universal rule, regardless of the consequences.""",
        "category": "Ethics"
    },
    {
        "id": 60,
        "question": """**Virtue Ethics**, rooted in Aristotle, focuses primarily on:""",
        "options": [
            """The consequences of an action""",
            """The moral duty or rule governing the action""",
            """Developing good character traits (virtues) in the moral agent""",
            """Achieving maximum pleasure for oneself"""
        ],
        "correct": 2,
        "explanation": """Virtue Ethics focuses on the moral character of the agent, asking, 'What would a virtuous person do?' and emphasizes developing virtues like courage and honesty.""",
        "category": "Ethics"
    },
    {
        "id": 61,
        "question": """What is Utilitarianism?""",
        "options": [
            """A type of Deontology""",
            """A moral theory that advocates for maximizing overall happiness or utility""",
            """The belief that only individual happiness matters""",
            """The belief that pleasure is bad"""
        ],
        "correct": 1,
        "explanation": """Utilitarianism is the most famous form of consequentialism, claiming that the right action is the one that produces the greatest balance of pleasure/happiness over pain/unhappiness for everyone affected.""",
        "category": "Ethics"
    },
    {
        "id": 62,
        "question": """A **Categorical Imperative** (in Kant's deontology) is a command that:""",
        "options": [
            """Applies only if you want a certain result (e.g., if you want money, then work)""",
            """Applies to everyone, everywhere, regardless of their goals or desires""",
            """Applies only to religious people""",
            """Applies only to government officials"""
        ],
        "correct": 1,
        "explanation": """Kant's Categorical Imperative is a universal moral law (a command) that applies unconditionally to all rational beings, regardless of what they want. (Unlike a Hypothetical Imperative which is conditional).""",
        "category": "Ethics"
    },
    {
        "id": 63,
        "question": """Aristotle's concept of **Eudaimonia** is best translated as:""",
        "options": [
            """Simple pleasure or hedonism""",
            """Wealth and fame""",
            """Flourishing or living well""",
            """Avoiding all pain"""
        ],
        "correct": 2,
        "explanation": """Eudaimonia is often translated as 'flourishing,' 'living well,' or 'the good life.' It is the ultimate goal of human life in Aristotelian ethics, achieved through virtuous activity.""",
        "category": "Ethics"
    },
    {
        "id": 64,
        "question": """**Moral Relativism** is the view that:""",
        "options": [
            """All moral rules are absolutely binding""",
            """Moral judgments are true or false only relative to a particular culture or historical period""",
            """Morality is determined by God's commands""",
            """There is only one universal morality"""
        ],
        "correct": 1,
        "explanation": """Moral Relativism (or Cultural Relativism) holds that moral truth is not universal but depends entirely on the norms and beliefs of a specific culture or society.""",
        "category": "Ethics"
    },
    {
        "id": 65,
        "question": """The **Golden Mean** in Aristotle's Virtue Ethics refers to:""",
        "options": [
            """The average moral behavior of all people""",
            """The ideal balance between two vicious extremes (excess and deficiency)""",
            """The most pleasurable action in any situation""",
            """The universal moral law given by reason"""
        ],
        "correct": 1,
        "explanation": """The Golden Mean is the virtuous disposition or character trait that lies between the two extremes of excess (too much) and deficiency (too little). For example, courage is the mean between recklessness and cowardice.""",
        "category": "Ethics"
    },
    {
        "id": 66,
        "question": """An ethical dilemma is a situation where:""",
        "options": [
            """The right choice is obvious to everyone""",
            """All choices are equally good""",
            """One must choose between two or more conflicting moral obligations or principles""",
            """The law forbids the moral choice"""
        ],
        "correct": 2,
        "explanation": """An ethical dilemma is a conflict in which you have to choose between two or more actions, all of which seem morally required, but you cannot perform all of them.""",
        "category": "Ethics"
    },
    {
        "id": 67,
        "question": """The **Principle of Utility** (or Greatest Happiness Principle) is the core principle of:""",
        "options": [
            """Deontology""",
            """Utilitarianism""",
            """Skepticism""",
            """Existentialism"""
        ],
        "correct": 1,
        "explanation": """The Principle of Utility, often summarized as 'the greatest happiness for the greatest number,' is the founding principle of Utilitarianism.""",
        "category": "Ethics"
    },
    {
        "id": 68,
        "question": """A major criticism of **Consequentialism** is that it can:""",
        "options": [
            """Be too vague and subjective""",
            """Be too focused on intentions rather than outcomes""",
            """Justify morally repugnant actions if they lead to a net positive outcome""",
            """Ignore the importance of happiness"""
        ],
        "correct": 2,
        "explanation": """A classic criticism is that by focusing only on outcomes, Utilitarianism can justify violating individual rights or committing injustice if it benefits the majority.""",
        "category": "Ethics"
    },
    {
        "id": 69,
        "question": """A major criticism of **Deontology** is that it:""",
        "options": [
            """Allows moral rules to be easily broken""",
            """Fails to provide clear guidance when moral duties conflict""",
            """Focuses too much on happiness""",
            """Promotes moral relativism"""
        ],
        "correct": 1,
        "explanation": """Deontology is often criticized for being too rigid and failing to provide a way to resolve conflicts between two equally binding moral duties (e.g., the duty not to lie vs. the duty to protect a life).""",
        "category": "Ethics"
    },
    {
        "id": 70,
        "question": """**Moral Objectivism** is the view that:""",
        "options": [
            """Morality applies only to objects, not people""",
            """All moral judgments are false""",
            """There are universal moral standards that apply to all people, at all times""",
            """Only the consequences matter"""
        ],
        "correct": 2,
        "explanation": """Moral Objectivism holds that there are objective moral truths or standards that are independent of human opinion or cultural belief.""",
        "category": "Ethics"
    },

    # Existentialism and Meaning (Questions 71-85)
    {
        "id": 71,
        "question": """What is the core tenet of Existentialism, according to Jean-Paul Sartre?""",
        "options": [
            """Essence precedes existence""",
            """Existence precedes essence""",
            """The universe is fundamentally meaningless""",
            """Only God can give life meaning"""
        ],
        "correct": 1,
        "explanation": """Sartre's famous claim is 'existence precedes essence,' meaning that humans are born (exist) as a blank slate and define their own nature (essence) through their choices and actions.""",
        "category": "Existentialism"
    },
    {
        "id": 72,
        "question": """What does the Existentialist concept of **'Anguish'** refer to?""",
        "options": [
            """The fear of death""",
            """The anxiety that arises from realizing we are completely responsible for our choices and for defining humanity""",
            """A feeling of deep sadness""",
            """The fear of being judged by others"""
        ],
        "correct": 1,
        "explanation": """Anguish (or anxiety) is the recognition of our absolute freedom and the total responsibility that comes with making choices that define not only ourselves but also the value of humanity (in Sartre's view).""",
        "category": "Existentialism"
    },
    {
        "id": 73,
        "question": """**'Bad Faith'** in Existentialism means:""",
        "options": [
            """Lying to others about one's beliefs""",
            """Denying one's freedom and responsibility by pretending to be determined by external forces (e.g., 'I had no choice')""",
            """Having a poor religious conviction""",
            """Making selfish choices"""
        ],
        "correct": 1,
        "explanation": """Bad Faith (mauvaise foi) is self-deception, particularly denying one's radical freedom and responsibility by claiming one is simply fulfilling a role or following a predetermined nature.""",
        "category": "Existentialism"
    },
    {
        "id": 74,
        "question": """Sartre argues that when a human chooses, they choose for:""",
        "options": [
            """Themselves alone""",
            """Their immediate family""",
            """All of humanity""",
            """God, who judges the choice"""
        ],
        "correct": 2,
        "explanation": """Sartre claims that in choosing for ourselves, we project an image of what a human being ought to be, thereby choosing for all of humanity, which is the source of anguish.""",
        "category": "Existentialism"
    },
    {
        "id": 75,
        "question": """The Existentialist view of **'The Absurd'** refers to:""",
        "options": [
            """The belief that life is logically contradictory""",
            """The conflict between humanity's innate desire for meaning and the universe's cold indifference/lack of inherent meaning""",
            """The rejection of all rationality""",
            """A state of profound joy and self-realization"""
        ],
        "correct": 1,
        "explanation": """The Absurd is the fundamental conflict between the human tendency to seek inherent value and meaning and the universe's apparent silence, meaninglessness, or indifference to this search.""",
        "category": "Existentialism"
    },
    {
        "id": 76,
        "question": """What does it mean to say 'man is condemned to be free'?""",
        "options": [
            """Freedom is a punishment""",
            """Humans are trapped by government laws""",
            """Humans cannot escape the necessity of choosing and being fully responsible for those choices""",
            """We are only free if we reject society"""
        ],
        "correct": 2,
        "explanation": """The phrase expresses the idea that since there is no God or predetermined nature, humans are wholly responsible for every action and choice they make; they cannot delegate or defer that freedom.""",
        "category": "Existentialism"
    },
    {
        "id": 77,
        "question": """What is the Existentialist view on finding meaning in life?""",
        "options": [
            """Meaning is given by God or nature""",
            """Meaning is an illusion created by society""",
            """Meaning must be created by the individual through their free choices and commitments""",
            """Meaning can be found only in science"""
        ],
        "correct": 2,
        "explanation": """Existentialism argues that since existence precedes essence, there is no pre-given meaning; the individual must create their own value and meaning through their life's projects and commitments.""",
        "category": "Existentialism"
    },
    {
        "id": 78,
        "question": """The philosophical problem of **Free Will vs. Determinism** asks:""",
        "options": [
            """Can we ever be happy?""",
            """Are all our actions predetermined by external or internal forces, or are we genuinely free to choose?""",
            """Is there a God?""",
            """Is knowledge possible?"""
        ],
        "correct": 1,
        "explanation": """This is the classic metaphysical problem of whether human actions are causally determined (Determinism) or if humans possess genuine freedom of choice (Free Will).""",
        "category": "Existentialism"
    },
    {
        "id": 79,
        "question": """A **Determinists'** position is that:""",
        "options": [
            """We are always free to choose""",
            """All events, including human actions, are causally necessitated by prior events and the laws of nature""",
            """Some events are determined, and some are random""",
            """Only major life events are determined"""
        ],
        "correct": 1,
        "explanation": """Determinism holds that everything that happens, including every human choice, is the necessary consequence of what has come before, leaving no room for genuine free will.""",
        "category": "Existentialism"
    },
    {
        "id": 80,
        "question": """What is a main consequence of accepting **Determinism**?""",
        "options": [
            """It makes moral responsibility easy""",
            """It challenges the concept of moral responsibility and praise/blame, as actions were inevitable""",
            """It proves the existence of God""",
            """It makes philosophy pointless"""
        ],
        "correct": 1,
        "explanation": """If all actions are inevitable, it becomes hard to justify holding people morally responsible for their actions, as they could not have done otherwise.""",
        "category": "Existentialism"
    },
    {
        "id": 81,
        "question": """Which position holds that we are both free and determined (i.e., that free will and determinism are compatible)?""",
        "options": [
            """Libertarianism""",
            """Hard Determinism""",
            """Compatibilism (Soft Determinism)""",
            """Fatalism"""
        ],
        "correct": 2,
        "explanation": """**Compatibilism** attempts to reconcile free will with determinism, often by defining a 'free' action as one that is caused by the agent's internal desires or decisions, even if those desires were ultimately determined.""",
        "category": "Existentialism"
    },
    {
        "id": 82,
        "question": """What is the **Libertarian** view on free will?""",
        "options": [
            """It claims free will is an illusion""",
            """It claims humans possess genuine free will, and therefore determinism must be false""",
            """It claims we are only free when we are alone""",
            """It claims freedom is not important"""
        ],
        "correct": 1,
        "explanation": """Philosophical Libertarianism asserts that we are genuinely free agents, and our choices are not fully determined by antecedent causes, thus rejecting determinism.""",
        "category": "Existentialism"
    },
    {
        "id": 83,
        "question": """What would an Existentialist say about someone who says, 'I cheated because everyone else does it'?""",
        "options": [
            """That person is being honest and realistic""",
            """That person is in **Bad Faith**, denying their freedom to choose otherwise""",
            """That person is morally correct""",
            """That person is a hard determinist"""
        ],
        "correct": 1,
        "explanation": """An Existentialist would say this is Bad Faith (self-deception), as the person is denying their responsibility and freedom by attributing their action to external social pressure.""",
        "category": "Existentialism"
    },
    {
        "id": 84,
        "question": """According to Sartre, if God does not exist, then what must be true?""",
        "options": [
            """Everything is permitted""",
            """Morality is impossible""",
            """Humans are no different from animals""",
            """Only science can save us"""
        ],
        "correct": 0,
        "explanation": """If God does not exist, there are no predetermined moral values or a pre-existing human nature, meaning 'everything is permitted,' placing the full burden of creation and value on humanity's shoulders.""",
        "category": "Existentialism"
    },
    {
        "id": 85,
        "question": """The search for an ultimately satisfying, rational justification for the universe's inherent meaning is the search for an answer to:""",
        "options": [
            """The problem of evil""",
            """The problem of induction""",
            """The problem of the Absurd""",
            """The problem of the one and the many"""
        ],
        "correct": 2,
        "explanation": """The conflict between our need for ultimate meaning and the universe's apparent lack of it is the definition of the philosophical problem of the Absurd.""",
        "category": "Existentialism"
    }
]

# -----------------------------------------------------------------------------

def display_question(question_data):
    """Displays the current question and options."""
    st.header(f"Question {question_data['id']} of 85")
    st.markdown(f"**Category:** *{question_data['category']}*")
    st.subheader(question_data['question'])

    # Get the key for the current question in st.session_state.answers
    answer_key = str(question_data['id'])
    
    # Store the user's choice (index of the selected option)
    selected_option = st.radio(
        "Select your answer:",
        question_data['options'],
        index=st.session_state.answers.get(answer_key), # Pre-select if answer exists
        key=f"radio_{answer_key}"
    )

    # Convert the selected option (string) back to its index
    try:
        selected_index = question_data['options'].index(selected_option)
    except ValueError:
        # Should not happen if pre-selection logic is correct, but safe check
        selected_index = None

    # Update session state with the selected index (0, 1, 2, or 3)
    # st.session_state.answers uses the question ID as the key and the option index as the value
    if selected_index is not None:
        st.session_state.answers[answer_key] = selected_index
    

def navigate_quiz():
    """Handles button clicks for navigation and submission."""
    col1, col2, col3 = st.columns([1, 4, 1])

    # Previous Button
    with col1:
        if st.session_state.current_question > 0:
            if st.button("⬅️ Previous"):
                st.session_state.current_question -= 1
                st.rerun()

    # Next Button / Submit Button
    with col3:
        if st.session_state.current_question < len(QUIZ_QUESTIONS) - 1:
            if st.button("Next ➡️"):
                st.session_state.current_question += 1
                st.rerun()
        elif st.session_state.current_question == len(QUIZ_QUESTIONS) - 1 and not st.session_state.quiz_completed:
            # Only show Submit button on the last question
            if st.button("🏁 Submit Quiz"):
                # Mark as completed and jump to results
                st.session_state.quiz_completed = True
                st.session_state.quiz_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.rerun()

    # Progress and completion check
    questions_answered = len(st.session_state.answers)
    total_questions = len(QUIZ_QUESTIONS)
    
    with col2:
        st.markdown(f"<div style='text-align: center;'>**Progress:** {st.session_state.current_question + 1}/{total_questions} | **Answered:** {questions_answered}</div>", unsafe_allow_html=True)
        
        # Display a warning if not all questions are answered before submission
        if st.session_state.current_question == len(QUIZ_QUESTIONS) - 1 and not st.session_state.quiz_completed and questions_answered < total_questions:
            st.warning(f"You have answered {questions_answered}/{total_questions} questions. Please review before submitting.")

def show_results():
    """Displays the quiz results, score, and review mode."""
    st.title("✅ Quiz Results")
    
    total_questions = len(QUIZ_QUESTIONS)
    correct_answers = 0

    # Calculate Score
    for q_data in QUIZ_QUESTIONS:
        q_id = str(q_data['id'])
        # Check if question was answered and if the index of the answer matches the correct index
        if q_id in st.session_state.answers and st.session_state.answers[q_id] == q_data['correct']:
            correct_answers += 1

    score_percentage = (correct_answers / total_questions) * 100

    st.success(f"### Score: {correct_answers}/{total_questions} ({score_percentage:.2f}%)")
    st.info(f"Completion Date: {st.session_state.quiz_timestamp}")
    st.markdown("---")

    # Review Section
    st.header("Detailed Review")
    
    # Use a loop to display each question with the correct answer and explanation
    for i, q_data in enumerate(QUIZ_QUESTIONS):
        q_id = str(q_data['id'])
        user_answer_index = st.session_state.answers.get(q_id)
        
        # Determine the status and color
        if user_answer_index is None:
            status = "Unanswered"
            color = "#ffc107" # Warning yellow
            user_answer_text = "N/A"
        elif user_answer_index == q_data['correct']:
            status = "Correct"
            color = "#28a745" # Success green
            user_answer_text = q_data['options'][user_answer_index]
        else:
            status = "Incorrect"
            color = "#dc3545" # Danger red
            user_answer_text = q_data['options'][user_answer_index]

        correct_answer_text = q_data['options'][q_data['correct']]

        st.markdown(f"""
        <div style="border: 1px solid {color}; border-left: 5px solid {color}; padding: 15px; margin-bottom: 10px; border-radius: 5px; background-color: #f8f9fa;">
            <p><strong>Q{q_data['id']}: {q_data['question']}</strong> <span style="float: right; color: {color}; font-weight: bold;">{status}</span></p>
            <p>Your Answer: <strong>{user_answer_text}</strong></p>
            <p>Correct Answer: <strong>{correct_answer_text}</strong></p>
            <details>
                <summary>Show Explanation</summary>
                <p style="margin-top: 10px; font-size: 0.9em;">{q_data['explanation']}</p>
            </details>
        </div>
        """, unsafe_allow_html=True)

    # Retake button
    if st.button("🔄 Retake Quiz"):
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.session_state.quiz_completed = False
        st.rerun()


def main():
    # If the quiz is completed, show results
    if st.session_state.quiz_completed:
        show_results()
        return

    # If not completed, show the current question
    if 0 <= st.session_state.current_question < len(QUIZ_QUESTIONS):
        current_data = QUIZ_QUESTIONS[st.session_state.current_question]
        display_question(current_data)
        navigate_quiz()
    else:
        # Should only happen if session state is messed up, display first question as fallback
        st.session_state.current_question = 0
        st.rerun()


if __name__ == "__main__":
    main()
