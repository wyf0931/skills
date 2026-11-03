# 解释文档的实践检查

## 同题案例：为什么超时后重试会重复执行

以下为自拟例子，具体去重保证取决于接口契约。

弱表达：“通过对幂等性的实现来进行重复执行问题的规避。”

改写：“请求超时后，客户端无法仅凭超时判断服务器是否已处理请求。如果直接重试，可能重复创建订单。幂等键（idempotency key）可用于识别同一次操作；具体去重范围取决于接口契约。”

这里依次交代现象、信息缺口、风险和机制。下一步可以讨论去重时限、不同请求的键以及失败重放的限制，但必须有资料支持。这不是每篇解释的固定结构。

验证问题：如果超时发生前服务器已成功写入，重试会怎样？如果换了幂等键，原来的推论是否仍成立？这些问题检查推理的边界，不代替技术测试。

## 常见失败

| 失败 | 修正 |
| --- | --- |
| 用另一个陌生概念解释当前概念 | 补上必要前提或换成读者已有知识 |
| 类比延伸成庞大故事 | 保留有用的对应关系，回到机制并说明边界 |
| 只说采用某设计“更好” | 说明目标、约束与代价；标明观点 |
| 推测某设计的优点，再当作历史动机 | 区分已知历史、当前机制和推断 |

## 实践来源

- [Julia Evans：Patterns in confusing explanations](https://jvns.ca/blog/confusing-explanations/)指出知识前提过期或前后矛盾会使解释失效。
- [Write good examples by starting with real code](https://jvns.ca/blog/2021/07/08/writing-great-examples/)介绍从真实代码中删去无关细节的方法。
- [Simple explanations without sounding condescending](https://jvns.ca/blog/2020/11/15/simple-explanations-without-sounding-condescending/)强调必要术语作为检索入口；[HN 讨论](https://news.ycombinator.com/item?id=25112163)提醒难易评价可能增加挫败感。

来源于 2026-11-03 查阅。这些是作者和评论者经验，不是普遍有效的实验结论。
