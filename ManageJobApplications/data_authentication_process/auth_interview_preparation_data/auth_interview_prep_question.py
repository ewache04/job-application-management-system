# ManageJobApplications/data_authentication_process/auth_interview_preparation_data/auth_interview_prep_question.py
def is_prep_question_data_valid(interview_preparation_data):
    if 'prep_questions' in interview_preparation_data:
        prep_questions = interview_preparation_data.get('prep_questions')
        if prep_questions and prep_questions.strip():
            return prep_questions
    return None

