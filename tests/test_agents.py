import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1] / 'src'))

from solo_unicorn_agents import (
    EngineeringAgent,
    DesignAgent,
    MarketingAgent,
    SalesAgent,
    SupportAgent,
)


def test_engineering_agent():
    agent = EngineeringAgent()
    assert agent.generate_code("feature X") == "Generated code for: feature X"
    assert agent.run_tests() == "Executed test suite"
    assert agent.manage_ci_cd() == "CI/CD pipeline executed"
    assert agent.monitor_system() == "System performance and security monitored"


def test_design_agent():
    agent = DesignAgent()
    assert agent.create_mockups("product Z") == "Created mockups for product Z"
    assert agent.generate_assets("logo") == "Generated asset: logo"
    assert agent.maintain_design_system() == "Design system and accessibility updated"


def test_marketing_agent():
    agent = MarketingAgent()
    assert agent.write_content("launch") == "Created content on launch"
    assert agent.perform_seo("ai startup") == "Optimized for keyword: ai startup"
    assert agent.analyze_campaign("summer campaign") == "Analyzed campaign: summer campaign"


def test_sales_agent():
    agent = SalesAgent()
    assert agent.qualify_lead("lead A") == "Qualified lead: lead A"
    assert agent.run_outreach("prospect B") == "Outreach sequence run for prospect B"
    assert agent.track_pipeline("deal C") == "Pipeline updated for deal C"


def test_support_agent():
    agent = SupportAgent()
    assert agent.resolve_ticket("password reset") == "Resolved ticket: password reset"
    assert agent.update_knowledge_base("reset process") == "Knowledge base updated with: reset process"
    assert agent.escalate_issue("login bug") == "Escalated issue: login bug"
