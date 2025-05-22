from app.core.scam_detection import ScamDetector
from app.services.llm_service import LLMService

def test_scam_detection_basic():
    llm = LLMService()
    detector = ScamDetector(llm)
    fake_offer = "This is a 100% guaranteed visa with no interview and only $500 processing fee."
    result = detector.analyze_offer(fake_offer)
    assert "scam" in result.lower() or "red flag" in result.lower()
