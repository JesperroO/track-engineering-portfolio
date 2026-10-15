# 银骥车队见面备忘｜2026-10-26

地点：珠海国际赛车场，银骥车队  
时间：2026-10-26 11:00  
对接人：欧阳富 Jack（Team Manager）

> 目的不是把问题逐条审问完，而是借聊天确认：银骥现在的技术体系到底成熟到什么程度、我能从哪里切入、有没有人可以带我，以及我能立刻贡献什么。

## 1. 先搞清楚 data / race engineering 现在是谁在做

- 车队平时的数据分析和 setup 工作主要是谁负责？
- Steve 是怎么认识 / 引入银骥的？
  - 长期合作，还是主要在 MSBK / 特定比赛时加入？
  - 他平时会不会参与珠海这边的数据、setup 或赛后复盘？
- 2025 跑 MSBK 时，data / setup 主要是谁负责？
- 2026 开始由 Steve 做 race engineering，是技术体系真的发生了变化，还是以前也有人做，只是今年官网第一次公开写？
- 除了 Steve，车队有没有固定的 engineer / data person / suspension specialist？

### 想确认的核心
银骥是不是正在从“资深技师 + 车手经验”为主，往更系统的  
**rider feedback → logger data → setup hypothesis → change → validation**  
这种工作流发展。

---

## 2. 马来西亚 / ZK Racing / MSBK 这条线

- 欧阳经理自己 2024 开始接触 MSBK 后，车队在技术流程上有没有明显变化？
- 银骥和 ZK Racing 现在是什么关系？
  - 只是送车手去训练？
  - 还是也有技术 / 工程人员之间的合作？
- JP、Alen 留在马来西亚训练时，除了 riding coaching，有没有接触当地的 engineer / data analysis？
- 银骥有没有考虑把马来西亚那边成熟的 data / setup 方法带回珠海？

---

## 3. 如果我参与，谁会 review / mentor 我

我目前能做：
- 数据整理、清洗、归档
- lap / sector comparison
- 视频与遥测同步
- braking point / throttle pickup / line / consistency 分析
- session comparison
- 基础车辆建模、分析脚本和工具
- 数据流程 / 数据库 / 自动化

我目前不应该独立负责：
- suspension setup 决策
- 根据 rider feedback 独立判断 rear/front instability 根因
- preload / compression / rebound / ride height 等车辆动态诊断
- 没有 review 的 setup recommendation

要问：
- 如果我前期参与，通常会有人一起看数据、review 我的判断吗？
- 我可以先从哪些工作开始？
- 哪些东西可以让我自己搭 / 自己 lead？
- 哪些技术判断必须由 Steve、技师或资深车手把关？

### 理想状态
我可以 lead：
- data pipeline
- session report
- telemetry / video workflow
- 数据库和工具

但 setup / vehicle dynamics judgement 前期需要 senior review。

---

## 4. 中山赛车场与银骥的关系

- 中山赛车场摩托车这块，银骥从什么时候开始深度参与？
- 银骥现在具体负责哪些部分：
  - 训练
  - GPR150 租车
  - 统一赛 / 港澳友谊赛
  - 赛事组织
  - 车手培养
  - 场地日常运营
- “银骥中山”团队和珠海总部是不是同一批人？
- GPR150 训练 / 统一赛平时有没有做 timing、数据记录、车手复盘？
- 如果我先从中山体系切入，会不会比直接跟 MSBK 更合适？

### 我的相关性
我自己长期用 Aprilia GPR150 跑赛道，并且已经基于这台车做 GNSS / IMU / OBD / 视频分析。

---

## 5. 外国车手 / 国际业务

银骥官网明显已经在面向外国车手提供：
- ZIC / 中国赛道信息
- 租车
- 赛道支持
- 报名 / 本地沟通
- 英文 / 日文内容

要问：
- 外国车手的咨询现在一般是谁负责？
- 英文沟通是谁做？
- 日文页面是谁维护？
- 网站三语内容是内部维护还是外包？
- 未来是否希望更多海外车手来 ZIC / 中山训练或参赛？

### 我可以立刻帮的部分
- 英文邮件 / 外国车手沟通
- 中英文资料整理
- 外国车手 onboarding / FAQ
- 活动报名材料和规则说明
- 国际客户信息整理

---

## 6. 网站 / 数据库 / digital ops

如果团队正在快速扩张，可以自然问：

- 现在车手、活动、报名、车辆、装备寄存、赛事记录主要怎么管理？
- 是微信群 + Excel + 人工记录为主吗？
- 有没有统一数据库 / CRM / 活动管理工具？
- telemetry / session 数据有没有统一的归档和索引？

我可以帮忙做：
- 官网维护和内容结构
- 多语言内容同步
- rider / client database
- CRM / foreign rider inquiry tracking
- 活动报名系统
- 车辆 / 装备寄存记录
- 赛事 / 训练记录
- telemetry / session 数据索引
- 自动生成 session report / basic dashboard

不要把自己说成“来做网站的”，而是把这部分作为能立即提供价值的第二入口。

---

## 7. 实际参与方式

要确认：
- 平时珠海 / 中山的测试、训练和比赛频率
- 最适合我从哪种活动开始跟
- 是否可以从：
  - 数据整理
  - session comparison
  - 计时 / session notes
  - 视频 / telemetry 同步
  - trackside support
  - 训练日 / 统一赛支持
  开始
- 如果合作顺利，能否逐步接触更正式的 CRRC / MSBK 项目

我的时间：
- 接下来几个月周末和假期可以稳定参与
- 部分工作日可以协调
- 希望持续参与，不是只体验一两次

---

## 8. 工作语言

自然聊到时问：
- 珠海和中山现场平时主要讲普通话还是粤语？
- 技术讨论 / 比赛现场如果有外国人，会不会切英文？
- 我普通话和英文没问题，粤语目前不会。

不要把粤语当成 blocker，先确认实际工作环境。

---

## 9. 需要观察，而不一定直接问

见面时留意：
- 有没有专门的数据电脑 / logger 下载流程
- 有没有 setup sheet / tyre sheet / session notes
- 数据是按 rider / bike / session 系统归档，还是比较散
- 技师和车手之间怎么讨论问题
- Jack 是否习惯把 rider feedback 转成具体 setup action
- Steve 是否留下过模板 / 流程 / 工具
- 中山与珠海两边的人手是否共享
- 团队目前最缺的是：
  - 数据人
  - 技师
  - 运营
  - 国际沟通
  - IT / 数据库
  - 现场人手

---

## 10. 如果被问“你能帮我们做什么”

可以直接答：

> 我现在最有把握的是把数据和现场信息整理得更系统，包括 session comparison、视频和遥测同步、驾驶表现分析、数据归档和分析工具。真正的 suspension setup 和车辆动态诊断我还在学习，所以我希望前期能跟着有经验的人一起看，先把我能做的部分做好，再逐渐把数据和 setup 判断连接起来。
>
> 另外如果你们现在外国车手、网站或者活动数据越来越多，我也能帮忙做英文沟通、网站维护、数据库和一些内部工具。

---

## 11. 这次见面的最低目标

不是拿到“实习 offer”。

最低成功标准：
1. 搞清楚银骥目前真正的 data / race engineering 组织方式。
2. 确认有没有人能带我学习 setup / vehicle dynamics。
3. 找到一个可以实际参与的第一个活动。
4. 让 Jack 明确知道我：
   - 会跑赛道
   - 有 GPR150 实车经验
   - 能做数据 / 工具
   - 知道自己目前不会什么
   - 愿意持续来
   - 还能补 international / digital ops 这一块
