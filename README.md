# 🔷 GraphQL Tools

AI GraphQL工具，支持Schema生成、查询优化、文档生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📋 Schema生成
- 🔧 Resolver生成
- ⚡ 查询优化
- 📦 Fragment生成
- 🎭 Mock数据生成
- 📖 文档生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from graphql_tools import create_tools

tools = create_tools()

# 生成Schema
schema = tools.generate_schema("博客系统")

# 生成Resolver
resolvers = tools.generate_resolvers(schema)

# 优化查询
optimized = tools.optimize_query(query, schema)

# 生成Fragment
fragments = tools.generate_fragments(schema, ["User", "Post"])

# 生成Mock数据
mock = tools.generate_mock_data(schema)

# 生成文档
docs = tools.generate_docs(schema)
```

## 📁 项目结构

```
graphql-tools/
├── tools.py       # GraphQL工具核心
└── README.md
```

## 📄 许可证

MIT License
