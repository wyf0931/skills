# 技术文档写作的社区实践资料

检索日期：2026-11-03。用途：为四个独立写作 skill 提供具体经验、反例与可执行规则，重点覆盖 Tutorial、How-to、Reference。Explanation 与中文适配见[实践综合与 skill 设计](skill-practice-synthesis.md)。

## 证据如何使用

- 社区帖子提供亲历问题、偏好和作者自述，不能据此声称某项做法已被普遍验证。点赞不作为有效性的证明。
- 项目官方页面提供可观察的写作案例，能证明页面采用了某种方法，不能单凭页面证明该方法改善了转化率或学习效果。
- 下文“候选规则”是本项目基于材料的归纳，尚需通过 skill 的实际输出验证。
- 日期采用页面明确显示的信息。部分 Reddit 页面只显示相对时间；未确认精确日期的条目明确保留该限制。公共 JSON 接口返回 403，未绕过访问限制。
- 优先保留具体失败、方法及反例；不把“某品牌文档最好”这类推荐直接变成规则。英文帖子均作中文短摘要，没有逐句翻译。

## 1. 参考中的示例应该解决什么问题

**来源**：[Ask HN: How do I write good documentation?](https://news.ycombinator.com/item?id=8414714)，2014-10-06。重点评论者 [ricardo_ramirez](https://news.ycombinator.com/item?id=8414758)、Fizzadar；发帖者是正在维护 PHP 框架的开发者。

**经验**：自学者提到 PHP 文档的小示例帮助他们使用接口；评论也提出对象如何创建、如何与其他组件交互、线程安全及实例化成本等实际查阅需求。

**候选规则 → Reference**：除签名和参数外，按对象性质补足调用前提、返回行为、副作用、生命周期及重要约束。示例应展示一个明确用法，减少读者自行猜测调用上下文。

**边界**：这些是个人学习经验与建议，不是所有接口必须填写的固定字段。线程安全只在并发语境有意义；实现历史与长篇设计取舍通常应链接至 Explanation。

## 2. 有示例仍然可能缺少文档

**来源**：[Examples are the best documentation](https://news.ycombinator.com/item?id=45532090)，2025-10-09，重点阅读 10 月 10 日 [harimau777 及其回复分支](https://news.ycombinator.com/item?id=45538265)，包括 bluGill、marcosdumay。

**冲突**：有人需要示例迅速判断能力；有人遇到偏离示例的输入后，需要明确参数、返回值和行为。线程中有人认为类型工具足够，也有人指出类型无法替代行为说明。

**候选规则 → Reference**：示例旁保留可独立查阅的行为契约。检查读者能否回答“换一个参数或输入会怎样”，避免只能照抄作者的路径。

**边界**：示例与参考的先后顺序取决于查阅情境；不规定必须先文字后代码。不要把某些生态的个人观察写成对整个生态的事实判断。

## 3. 被喜欢的文档，具体好在哪里

**来源**：[Ask HN: Best examples of software documentation that you've come across?](https://news.ycombinator.com/item?id=34820382)，2023-02-16。重点评论者 mauvehaus、someotherperson、[hangonhn](https://news.ycombinator.com/item?id=34821775)。

**具体观察**：评论分别认可 PostgreSQL 保留旧版本文档、Django 文档之间的链接、Redis 命令页的版本和复杂度信息。其他评论也提醒同一厂商的页面质量可能差异很大。

**候选规则 → Reference / 全部类型**：内容有版本差异时注明适用版本；需要跨类型阅读时链接到具体目标页。评估具体页面和任务，不照搬“某站点是金标准”的品牌结论。

**边界**：社区评价属于偏好；下文只核实其中可直接观察的写法。版本信息、复杂度不应机械添加到无关对象。

## 4. 失效的示例与接口说明如何伤害真实项目

**来源**：[Our startup has docs issues and it is costing us prospects](https://www.reddit.com/r/ExperiencedDevs/comments/13jh3zf/our_startup_has_docs_issues_and_it_is_costing_us/)，2023 年，精确日期未在本次打开页面中确认。

**亲历问题**：发帖的创始工程师报告，潜在客户抱怨文档，团队发现关键工作流缺指南、示例不更新、React SDK 参考过时。[ccb621](https://www.reddit.com/r/ExperiencedDevs/comments/13jh3zf/comment/jkf6cwr/) 等评论者建议把文档纳入完成条件、测试示例，并让新人从头使用、记录阻塞点。

**候选规则 → Tutorial / How-to / Reference**：交付时注明已核验的环境及版本；能运行的示例实际运行；无法验证的明确列出。复核教程时从空环境走完，记录安装、凭证、目录和隐含依赖造成的阻塞。

**边界**：评论中的“可执行/生成文档永不过时”是过强结论。测试可以发现执行失败，不能自动发现误导性描述、缺失场景、无效的学习顺序。具体发布门禁属于团队流程，写作 skill 不应擅自修改 CI。

## 5. “适合初学者”必须说清楚初学什么

**来源**：[Good documentation to learn from?](https://www.reddit.com/r/learnpython/comments/1koiwtm/good_documentation_to_learn_from/)，2025 年，精确日期未确认。重点看发帖者补充与 [Gshuri 的回复](https://www.reddit.com/r/learnpython/comments/1koiwtm/comment/msrks7b/)。

**亲历问题**：初学者阅读 Python 官方教程时，被尚不熟悉的术语和概念卡住；回复指出“有编程经验、刚学 Python”和“从未编程”是不同受众。

**候选规则 → Tutorial**：开写前用可观察能力描述起点，例如“能运行 Python 脚本”，避免仅写“零基础”“适合新手”。出现前置概念时，要么提前铺垫，要么链接到补充学习路径。

**边界**：不采纳线程中责备读者的语气。受众不匹配不等于文档写得差，更不意味着文档理应难懂。此处有官方页面直接支持其受众定位，见案例 A。

## 6. 采用 Diátaxis 后，新功能并不自动获得一篇新页面

**来源**：[Implementing Diataxis framework](https://www.reddit.com/r/technicalwriting/comments/1vreuj2/implementing_diataxis_framework/)，检索索引列出 2026 年讨论，本次正文仅显示相对时间，精确发帖日期未确认。重点评论者 HSButtNaked、[the_nameless_nomad](https://www.reddit.com/r/technicalwriting/comments/1vreuj2/comment/p4mo6rq/)、tw15tw15。

**实施经验**：评论者自述，新功能经常被误当作新页面；另一位在多家公司实施过的作者认为 How-to 和 Reference 较容易先改，Tutorial 更费时，并明确承认用户正面反馈不能归因于 Diátaxis 一项改动。还有人提醒读者可能从搜索直接进入。

**候选规则 → 四个 skill**：写新页前检查现有文档是否已覆盖同一读者任务；据任务选择补写、更新或新建。页面需要让直接进入的读者知道适用条件及相关入口。

**边界**：不是所有项目都应该最后写教程，也不能从作者自述推出框架能减少认知负荷的因果结论。

## 7. 四类内容不能直接替代信息架构

**来源**：[Diátaxis — is there anything you'd like to know?](https://www.reddit.com/r/technicalwriting/comments/1gqksi1/di%C3%A1taxis_is_there_anything_youd_like_to_know/)，主帖 2024-11-13，回复跨多个时间。发帖账号 EvilDMP 自述为框架作者。

**作者建议**：大量操作指南可以再按生命周期或工作情境分组，例如准备、部署、扩容，或计划内、突发、紧急操作。讨论中也区分了帮助理解与面向选型的价值说明。

**候选规则 → How-to / 诊断能力**：按读者寻找任务的方式设计标题和分组；不能要求读者先学会四个术语才找得到内容。

**边界**：这些是作者的设计判断，不是分组数量的定量阈值。写单篇文章时通常无需扩展到全站导航重构。

## 可直接检查的一方案例

### A. Python 官方教程的受众声明

[The Python Tutorial](https://docs.python.org/3/tutorial/)，2026-11-03 查阅，动态版本页。

页面明确面向已有编程经验、刚接触 Python 的读者，并说明不追求涵盖所有功能，同时链接标准库和语言参考。这支持“受众起点具体化”和“主动声明覆盖边界”的写法，不证明它适合所有初学者。

### B. Django 5.2 首个应用教程

[Writing your first Django app, part 1](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)，固定 5.2 文档，2026-11-03 查阅。

开头给出投票应用的成果，随后检查安装版本，说明版本不符时去哪里，再给项目目录和操作。可借鉴“成果—环境检查—具体行动—可观察结果”的衔接。它不是必须逐项复制的通用模板；当前任务若已经完成安装，应避免重复无关流程。

### C. Django 5.2 部署清单

[Deployment checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)，固定 5.2 文档，2026-11-03 查阅。

页面按部署目标列出检查项，提供自动检查命令，区分开发与生产条件，并在具体设置旁给出风险说明。它展示了 How-to 可以采用清单，不必强行写成从第一步到最后一步的单一路径。必要的简短理由有助于正确选择操作。

### D. Redis SCAN 命令参考

[SCAN](https://redis.io/docs/latest/commands/scan/)，动态 latest 页，2026-11-03 查阅。

页面提供语法、引入版本、单次与完整遍历的复杂度，并展开迭代保证及限制。它展示了 Reference 的价值可以来自精确的行为边界；仅有类型和成功示例不足以表达全部使用约束。这里提炼写作方法，不作为某个目标 Redis 版本的技术规格。

## 对首版 skill 的具体建议

以下为本项目的综合判断，而非任何一篇帖子的原话。

| Skill | 应补充的实践能力 | 建议行为验证 |
|---|---|---|
| Tutorial | 写清能力起点；检查概念依赖；连通环境、文件、命令、结果；给观察点 | 让未读其他页面的目标读者从指定起点走完；记录需猜测的位置 |
| How-to | 按真实任务写标题；在操作前给选择条件；包含必要分支和完成判断；允许清单结构 | 给出两个不同但合理的初始状态，检查读者是否能选对路径 |
| Reference | 说明行为契约及重要限制；示例不替代定义；注明相关版本；链接具体任务指南 | 提问示例未覆盖的输入、默认值或边界条件，检查是否能查到答案 |
| Explanation | 说明设计选择的理由，避免把教程步骤或参数清单混入主体 | 用具体疑问检验是否解释了因果、取舍与适用边界；另见[实践综合](skill-practice-synthesis.md) |

不建议把社区讨论整篇塞进 `SKILL.md`。入口保留会改变写作决策的规则；来源、反例和同题改写适合放进按需读取的 references。源链接应留在研究材料中，便于回看上下文及后续修正。
