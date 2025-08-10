from agents import (
    EngineeringAgent,
    DesignAgent,
    MarketingAgent,
    SalesAgent,
    SupportAgent,
)


def test_engineering_agent():
    agent = EngineeringAgent()
    assert agent.generate_and_refactor_code("print('hi')  ") == "print('hi')"
    assert agent.write_and_run_tests([lambda: 1 + 1 == 2]) is True
    assert agent.manage_deployments_and_ci_cd(["build", "deploy"]) == [
        "build executed",
        "deploy executed",
    ]
    metrics = {"performance": 0.9, "security": 1.0}
    assert agent.monitor_performance_and_security(metrics) == metrics


def test_design_agent():
    agent = DesignAgent()
    mockups = agent.produce_mockups(["button"])
    assert mockups["button"] == "mockup for button"
    assert agent.generate_assets(["logo"]) == ["logo.png"]
    guidelines = {"color": "#fff"}
    assert agent.maintain_design_system(guidelines) is guidelines


def test_marketing_agent():
    agent = MarketingAgent()
    assert agent.write_blog_post("feature X") == "Blog post about feature X"
    keywords = agent.perform_seo_research("test")
    assert "test tips" in keywords
    metrics = agent.analyze_campaign(100, 25)
    assert metrics["ctr"] == 0.25


def test_sales_agent():
    agent = SalesAgent()
    lead = {"budget": 1000, "interest": True}
    assert agent.qualify_lead(lead) is True
    sequence = agent.run_outbound_sequence("Alice")
    assert sequence[0].startswith("Introductory")
    pipeline = agent.track_pipeline(["Lead1"])
    assert pipeline == ["Lead1"]


def test_support_agent():
    agent = SupportAgent()
    assert "Forgot password" in agent.resolve_ticket("How do I reset my password?")
    agent.update_knowledge_base("New question", "New answer")
    assert agent.resolve_ticket("New question") == "New answer"
    assert agent.escalate_issue("bug") == "Escalated: bug"
