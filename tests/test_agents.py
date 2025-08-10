from agents import (
    EngineeringAgent,
    DesignAgent,
    MarketingAgent,
    SalesAgent,
    SupportAgent,
)


def test_engineering_agent():
    agent = EngineeringAgent()
    assert agent.generate_code("feature X", "Python") == "Generated Python code for feature X."
    assert agent.write_tests("module Y") == "Wrote tests for module Y."
    assert agent.deploy("staging") == "Deployed to staging."
    assert agent.monitor("service Z") == "Monitoring service Z."


def test_design_agent():
    agent = DesignAgent()
    assert agent.create_mockup("product Z") == "Created mockup for product Z."
    assert agent.generate_logo("brand A") == "Generated logo for brand A."
    assert agent.check_accessibility("component B") == "Checked accessibility for component B."


def test_marketing_agent():
    agent = MarketingAgent()
    assert agent.write_content("feature Q") == "Wrote content about feature Q."
    assert agent.perform_seo_research("keyword K") == "Researched SEO for keyword K."
    assert agent.analyze_campaign("campaign C") == "Analyzed campaign campaign C."


def test_sales_agent():
    agent = SalesAgent()
    assert agent.qualify_lead("lead L") == "Qualified lead lead L."
    assert agent.run_sequence("prospect P") == "Ran outreach sequence for prospect P."
    assert agent.track_pipeline("deal D") == "Tracked deal deal D."


def test_support_agent():
    agent = SupportAgent()
    assert agent.resolve_ticket(42) == "Resolved ticket 42."
    assert agent.update_knowledge_base("topic T") == "Updated knowledge base with topic T."
    assert agent.escalate("issue I") == "Escalated issue issue I to engineering."
