from __future__ import annotations

from typing import List


class AgentOrchestrator:
    def __init__(self, config):
        self.config = config

    def build_prompt(self, user_goal: str, style: str | None = None) -> str:
        style_text = style or self.config.desired_style
        return (
            f"You are a 3D art director and expert modeler. "
            f"Goal: {user_goal}. "
            f"Style: {style_text}. "
            "Follow these priorities: organic flow, sculptural surfaces, curved transitions, material richness, and believable detail. "
            "Use realistic proportions, natural imperfections, and expressive form. "
            "Do not settle for simple boxes or flat geometry."
        )

    def expand_prompt(self, user_goal: str) -> List[str]:
        prompts = [
            self.build_prompt(user_goal),
            self.build_prompt(user_goal, "curved, highly detailed, realistic, natural textures"),
            self.build_prompt(user_goal, "industrial but organic, smooth transitions, complex forms"),
        ]
        return prompts
