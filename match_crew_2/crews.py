from candidate_matcher.crew import CandidateMatchCrew
from candidate_searcher.crew import CandidateSearchCrew
from job_matcher.crew import JobMatchCrew

class MatchCrew:

    def __init__(candidate_list, jobs_list):
        self.candidate_list = candidate_list
        self.jobs_list = jobs_list


    def run_candidate_match(job_description):
        inputs = {
            'candidates_list': self.candidate_list,
            'job_query': job_description
        }

        return CandidateMatchCrew.crew().kickoff(inputs=inputs)


    def run_candidate_search(query):
        inputs = {
            'candidates_list': self.candidate_list,
            'query': query
        }

        return CandidateMatchCrew.crew().kickoff(inputs=inputs)


    def run_job_match(candidate):
        inputs = {
            'jobs_list': self.jobs_list,
            'candidate': candidate
        }

        return CandidateMatchCrew.crew().kickoff(inputs=inputs)