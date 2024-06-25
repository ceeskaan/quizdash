from typing import List
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from components.model import llm


class Question(BaseModel):
    question: str
    answer: str
    explanation: str
    options: List[str]


class Quiz(BaseModel):
    title: str
    n_questions: int
    n_options: int
    difficulty: str
    quiz: List[Question]


parser = PydanticOutputParser(pydantic_object=Quiz)


def LLM_generate_quiz(topic, n_questions, n_options, difficulty):

    prompt = PromptTemplate(
        template="""You are an expert Quiz Generator. 
            Generate a {difficulty} multiple-choice quiz, give me {n_questions} questions and answers about {topic}.
            Each question should have {n_options} options. Make 100%% sure that there is only one correct option and that this is one of the {n_options} options.
            With every question, also give a brief explanation on why this is the right answer and the others are not.
            Give the quiz a title based on the topic. \n{format_instructions}\n""",
        input_variables=["topic", "n_questions", "n_options", "difficulty"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | llm | parser
    output = chain.invoke({"topic": topic, "n_questions": n_questions, "n_options": n_options, "difficulty": difficulty}).dict()
    
    return output