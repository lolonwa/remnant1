from app.services.llm_service import LLMService
from app.core.scam_detection import ScamDetector

def test_scam_detector():
    llm = LLMService()
    scam_detector = ScamDetector(llm)

    # Sample suspicious offer text
    offer_text = """
    Congratulations! You have been pre-approved for a work visa in CountryX.
    Just send us $500 as a processing fee and your passport details.
    No interview needed. This offer is 100% guaranteed.
    """

    result = scam_detector.analyze_offer(offer_text)
    print("Scam Detection Result:")
    print(result)

if __name__ == "__main__":
    test_scam_detector()
