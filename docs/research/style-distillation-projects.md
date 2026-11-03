# 开源文风蒸馏项目：实现核对

研究日期：2026-11-03。用途是为中文政策、政府宣传和古文方向选择实现方法，不是推荐直接安装，也未完成这些项目的端到端运行评测。

## 检索与核对范围

搜索了 GitHub、Reddit，以及面向 HN、X 的定向查询。社区帖子只用于发现项目；下面的技术判断依据固定提交的文件树、入口和实际脚本。没有把搜索摘要、项目星数或第三方打分当作效果证据。X 定向查询未取得可据以核实实现的第一方帖子；本记录不伪造 X 社区共识。

[Reddit 的 Write-Like-Me 发布帖](https://www.reddit.com/r/claudeskills/comments/1tam2t4/writelikeme_a_claude_code_skill_that_analyzes/)明确链接 `Hiro-Inagawa/write-like-me`，是本轮最有价值的社区线索。页面只显示相对时间，未推算精确发布日期。项目同名较多，以下始终使用 owner/repo 标识。

## 1. Hiro-Inagawa/write-like-me：真正带确定性测量的混合方案

快照：`9ea50a0e6be96b668354bc1112d8a6139550bf66`，仓库声明 MIT。

**实际框架**：语料与语域筛选 → 本地文体特征 → Agent 规则提炼与例文选择 → 命名 voice/profile → 确定性草稿检查 → golden 回归。基础统计使用标准库，可选 textstat 与 spaCy；语义解释和写作仍由 Agent 完成。

**真实计算**：句长分布、功能词频率、标点、MATTR、段落和句首模式等。`voice_eval.py` 的评估对象主要是规则检查器：召回、误报和噪声，而非证明生成稿整体文风相似。内容高频词函数也明确说明不是真正 TF-IDF。

**中文限制**：词元正则仅匹配拉丁字母，句切分依赖英文句号及空白，大模型相关可选分析使用 `en_core_web_sm`。不能仅把提示词改成中文便复用数值结果。

来源：[入口](https://github.com/Hiro-Inagawa/write-like-me/blob/9ea50a0e6be96b668354bc1112d8a6139550bf66/SKILL.md)、[统计代码](https://github.com/Hiro-Inagawa/write-like-me/blob/9ea50a0e6be96b668354bc1112d8a6139550bf66/scripts/stylometry.py)、[评估说明](https://github.com/Hiro-Inagawa/write-like-me/blob/9ea50a0e6be96b668354bc1112d8a6139550bf66/eval/README.md)。

**本次小检查**：从统计脚本以 AST 只选取两个无副作用函数，在内存执行；输入自拟文本“推动产业发展。完善服务体系。加强组织保障。”，得到空词元列表和一个整段“句子”。这是中文边界检查，不是完整程序运行或效果评测。

可借鉴：测量与规则分离、按语域分别建立分布、规则检查器本身也测误报。不可直接照搬英文特征、最小词数和统一反 AI 基线。

## 2. Wang-Ruibin/paper-alchemist：本地种子与语义审核分离

快照：`6f8f530ee559cf345d0bbdbb6fd4ae6772131bd3`，仓库声明 MIT。

**实际框架**：文档抽取、章节识别、量化种子、Agent 语义观察、模块综合、生成前验证。代码负责来源与片段哈希、语料清单及状态；脚本不直接调用 LLM API。当前入口明确为 Codex-only，搜索索引中的旧跨平台描述不能作为当前支持结论。

**真实计算**：中文句长以字符为单位，另统计引用、限定语、第一人称和图表提及。语义观察须绑定现存来源与片段哈希；种子状态为 pending，不能把自动抽取完成当成蒸馏完成。分组划分代码还将重复相关材料放在同组，避免直接跨开发/保留集。

**边界**：学术模块、字数过滤及固定 70/30 跨语言指导不应搬入中文政策或古文方案。近重复分组的 8-word shingle 仍按拉丁字母取词，不能假定已覆盖中文近重复；精确哈希分组则与语言无关。本次核对代码与状态机制，未验证其学术写作效果。

来源：[入口](https://github.com/Wang-Ruibin/paper-alchemist/blob/6f8f530ee559cf345d0bbdbb6fd4ae6772131bd3/skills/paper-alchemist/SKILL.md)、[文本统计](https://github.com/Wang-Ruibin/paper-alchemist/blob/6f8f530ee559cf345d0bbdbb6fd4ae6772131bd3/engine/sections.py)、[观察审核](https://github.com/Wang-Ruibin/paper-alchemist/blob/6f8f530ee559cf345d0bbdbb6fd4ae6772131bd3/engine/observations.py)、[语料划分](https://github.com/Wang-Ruibin/paper-alchemist/blob/6f8f530ee559cf345d0bbdbb6fd4ae6772131bd3/engine/corpus.py)。

可借鉴：统计输出只是证据种子；语义审核状态可追踪；统计特征按语言定义，来源变化使旧观察失效。

## 3. duzhihan/StellarTrack 的 writing-dna-skill：分层清晰，统计实现未随包提供

快照：`ff641435cec031fc997af5e55dab84c8cfe61549`，skill 内有 MIT 许可文件。

**实际框架**：完整文章与元数据 → 表层语言、结构、选题、素材、认知、视觉六层观察 → 四份专题文档与 Writing-DNA 整合。明确将词频、句长、标点交给脚本统计，结构与认知交给阅读归纳，提供中文模板。

**实现核对**：当前 skill 文件树主要为 Markdown、模板和 schema，没有随包统计脚本。因此“脚本统计”是给 Agent 的工作要求，不能等同于已有可复现测量器。二十篇、固定名词/动词清单等是作者流程设定，未见对应有效性证明。

**中文适配价值**：六层分工有启发，但我们的目标不必包含视觉、世界观与选题模仿；尤其要防止把样本立场当成写作规则。未发现针对古文的独立计算方法或有效性评测。

来源：[入口](https://github.com/duzhihan/StellarTrack/blob/ff641435cec031fc997af5e55dab84c8cfe61549/skills/writing-dna-skill/SKILL.md)、[包目录](https://github.com/duzhihan/StellarTrack/tree/ff641435cec031fc997af5e55dab84c8cfe61549/skills/writing-dna-skill)。

可借鉴：分层观察和元数据。不能当成现成词频引擎直接迁移。

## 4. Guan-Yep/style-distiller：合同化输出与按需检索

快照：`4a288008bf3491b75ab3c203f05f4058065c60fb`，仓库声明 MIT。

**实际框架**：参考文档分类 → 结构与风格分析 → 可检索的合同文件 → 自包含 skill 包。重视文档类型、格式和信息结构；输出入口通过检索参考合同来减少一次性加载。

**脚本职责**：唯一的 `init_distillation.py` 建目录、写待填模板、保存状态，是初始化器，不是文风特征提取器。观察与归纳仍依赖 Agent。固定要求大量检索指令、文档格式合同等，偏重说明书和报告，也增加交付重量。

**可借鉴范围**：可复用规则应该有来源、可独立运行、按需加载；不宜为了原子化而预先制造许多空合同。没有以此证明中文政策、宣传或古文的迁移效果。

来源：[入口](https://github.com/Guan-Yep/style-distiller/blob/4a288008bf3491b75ab3c203f05f4058065c60fb/SKILL.md)、[初始化器](https://github.com/Guan-Yep/style-distiller/blob/4a288008bf3491b75ab3c203f05f4058065c60fb/scripts/init_distillation.py)。

## 5. jianshuo/claude-skills 的 wjs-distilling-style：中文锚点卡与模型判官

快照：`114fbcf7e0ffdd37d8b6a7aed4347f9427b4a1c9`，仓库声明 MIT。

**实际框架**：样本 → 九轴 Style Card（观察、规则、原句）→ 保持事实骨架的改写 → 可选多轮独立模型判官。当前入口默认采用一次 prompt 与内联自检，完整盲测为较重路径。该子目录没有确定性统计代码。

**可借鉴点**：明确分离怎么写与内容立场；用原句锚定可执行规则；相似度要求不能授权新增事实。仓库别处虽有 `expression_stats.py`，但它服务另一项 skill，使用英文分词和句子逻辑，不能算这个蒸馏器已实现中文测量。

**评测边界**：其异模型判官与“真迹/生成稿”分类是模型评价，不能代替读者盲评或事实审核。平衡样本上分类准确率低于或等于 50% 也不是普遍成功标准，须排除标签、类别偏差与样本量问题。项目的自述轮次不能视为独立复现。

来源：[入口](https://github.com/jianshuo/claude-skills/blob/114fbcf7e0ffdd37d8b6a7aed4347f9427b4a1c9/wjs-distilling-style/SKILL.md)、[另一项 skill 的统计脚本](https://github.com/jianshuo/claude-skills/blob/114fbcf7e0ffdd37d8b6a7aed4347f9427b4a1c9/wangjianshuo-perspective/scripts/expression_stats.py)。

## 跨项目结论

以下为本项目的设计推导，不是上述项目共同证明的事实。

1. **不应把“带统计术语”误认成“有统计实现”。**本轮样本中，真正明确绑定本地计算的两个项目，比纯提示词或模板流程更接近我们想要的方向；但尚不能直接覆盖目标中文文体。
2. **保留技术层，缩小运行引擎。**可以让脚本稳定负责样本清单、去重、分句、分布、候选表达与来源定位，让 Agent 负责语义解释、适用边界与规则编写；无需为此保留抓取器与额外 LLM API 客户端。
3. **量化特征不直接变成写作命令。**发现短句比例、某个连接词频率或排比候选后，应输出测量口径、分布、覆盖文档和上下文，再判断其是否值得迁移。没有出现的特征不自动成为禁令。
4. **中文应重做测量口径。**政策文本、宣传文章、文言作品和现代古文解读应分组；编辑加上的标点和标题需要元数据，古文的断句差异不能被当作作者节奏。通用英文可读性指标不能直接沿用。
5. **不同检查分开报告。**脚本正确性、特征稳定性、风格迁移、人类可读性与事实忠实度是不同对象。规则检查器过关，不能推出文章整体好；模型判官说像，也不能推出内容正确。

首版可以是一个独立 skill 加一个小型、无 API 的中文分析脚本。这里的“轻量”应减少依赖与重复流程，不应删掉可重复的测量和证据。
