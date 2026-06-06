"""
GraphQL Tools - AI GraphQL工具
支持Schema生成、查询优化、文档生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class GraphQLTools:
    """
    AI GraphQL工具
    支持：Schema、查询、文档
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_schema(self, description: str) -> str:
        """生成GraphQL Schema"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下描述生成GraphQL Schema：

{description}

要求：
1. 类型定义
2. 查询类型
3. 变更类型
4. 输入类型"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_resolvers(self, schema: str) -> str:
        """生成Resolver代码"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下Schema生成Resolver代码：

{schema}

要求：
1. Python实现
2. 异步支持
3. 错误处理
4. 数据加载"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def optimize_query(self, query: str, schema: str) -> Dict:
        """优化查询"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请优化以下GraphQL查询：

Schema：{schema[:500]}
查询：{query}

请返回JSON格式：
{{
    "optimized_query": "优化后的查询",
    "issues": ["问题1", "问题2"],
    "improvements": ["改进1", "改进2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimization": content}

    def generate_fragments(self, schema: str, entities: List[str]) -> str:
        """生成Fragment"""
        if not self.client:
            return "LLM客户端未配置"

        entities_text = ", ".join(entities)

        prompt = f"""请为以下实体生成GraphQL Fragment：

Schema：{schema[:500]}
实体：{entities_text}

请返回完整的Fragment定义："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_mock_data(self, schema: str) -> str:
        """生成Mock数据"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请根据以下Schema生成Mock数据：

{schema[:1000]}

请返回JSON格式的Mock数据："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_docs(self, schema: str) -> str:
        """生成文档"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下GraphQL Schema生成文档：

{schema[:2000]}

要求：
1. 类型说明
2. 查询示例
3. 变更示例
4. 最佳实践"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> GraphQLTools:
    """创建GraphQL工具"""
    return GraphQLTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("GraphQL Tools")
    print()

    # 测试
    schema = tools.generate_schema("博客系统，包含用户、文章、评论")
    print(schema[:300] + "...")
