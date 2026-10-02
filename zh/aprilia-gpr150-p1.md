# aprilia GPR150 / P1：实车采集与性能分析

[中文首页](../README.zh-CN.md) · [English](../case_studies/p1-gpr150-telemetry.md)

**2026 年 9 月 · P1 国际赛车场 · 独立骑行、采集与分析 · 九节练习、71 个计时圈**

我用 RaceChrono、GPS、OBD、心率带和车载影像记录自己的赛道练习。我重点比较刹车点后移以后，是否更晚入弯、更早开油，以及这个弯省下的时间会不会在后面的连续弯丢掉。

## 刹车参照、入弯与开油

我把各圈轨迹对齐到自己拍摄的 P1 赛道板，在图上标出开始减速、倾角变化和开油的位置。将 47 个可比较的计时圈按练习顺序排列后，可以看到刹车点如何逐步后移，以及同一节里各圈的刹车点是否稳定。

![T2 线路与刹车参照对比](../assets/p1/p1-t2-board-reference.png)

S02 L2 与 S08 L8 的减速起点相差 **12.3 m**，后者更靠近主左弯；达到 20° 倾角的位置仍接近。最低速度之后，持续达到 40% 油门的时间从 **1.50 s 缩短到 0.10 s**。

[![播放 T2 同步车载片段](../assets/p1/aprilia-gpr150-t2-braking-reference.jpg)](https://raw.githubusercontent.com/JesperroO/track-engineering-portfolio/core/assets/p1/aprilia-gpr150-t2-braking-reference.mp4)

这段 **20 秒 S04 影像**展示了 T1 路肩凸起、直道后的 T2 主左弯和驾驶过程，叠加速度、转速、油门、估算倾角与加减速 G 值，保留发动机原声。影像中的路肩凸起是我逐步尝试后采用的刹车参照。

[完整 T2 分析与参照演变](../case_studies/p1-gpr150-analysis.md#t2-lines-control-and-reference-development) · [视频对齐与实景参照](../case_studies/p1-gpr150-analysis.md#t2-onboard-example-developing-a-repeatable-braking-reference)

## 连续弯：一个弯快了，后面会不会慢

我在赛道上选定固定位置划分区段，对照线路、速度、油门和左右倾角，比较整组连续弯。

![连续弯的实测线路对比](../assets/p1/p1-linked-board-lines.png)

S06 L7 与 S08 L8 的比较中，一个区段节省 **0.431 s**，接下来的转向衔接却损失 **0.461 s**。对比图同时标出右弯线路、开油后再次收油，以及从右倾转向左倾的过程。

最后两个 PB 之间的 **0.424 s** 改善，主要来自 G20–G40 的 **0.371 s**。我按固定分段累计时间差，并放大比较 G20–G40 的线路、速度和控制动作。

[连续弯分析](../case_studies/p1-gpr150-analysis.md#1-linked-sequence-a-quicker-right-hand-block-can-cost-the-next-transition) · [连续两个 PB 的分段时间差](../case_studies/p1-gpr150-analysis.md#2-s08-consecutive-pbs-where-the-final-0424-s-came-from)

## OBD、倾角与心率

我将 GPS 速度、OBD 转速和换算到 0–100% 的油门数据对齐，再以最低速度时刻或固定赛道位置比较各圈。即使出弯速度接近，转速也可能不同：S07 L5 出口约 **7,106 rpm**，S08 L8 约 **9,346 rpm**。

![出弯速度、转速与油门时序](../assets/p1/p1-obd-engine-recovery.png)

倾角分析比较最大倾角，以及保持较大倾角的时间。心率分析比较减速前后的变化，再查看这种变化在不同节、不同圈里是否反复出现。其他对比包括 S09 右弯练习、挡位选择，以及同一节内连续两圈的线路和操作。

[OBD、倾角与心率分析](../case_studies/p1-gpr150-analysis.md#obd-control-timing-and-rider-state-analysis) · [挡位与同节对比](../case_studies/p1-gpr150-analysis.md#supporting-driving-and-setup-comparisons)

## 数据采集与复盘

采集设备和软件包括 RaceChrono、GPS／IMU、胸部心率带、vLinker MC+ BLE OBD2 和 DJI Action 5 Pro 头盔影像。我用 Circuit Tools 3 在 P 房笔记本上复盘，赛后继续完成多机位与遥测对齐。

页面附有同步视频、减速与开油位置图、线路和操作曲线、分段时间差及汇总数据。S04–S07 连续骑行，分析在赛后完成；有休息间隔时，我在 P 房复盘并安排下一节练习。

[详细分析](../case_studies/p1-gpr150-analysis.md) · [测量方法](../case_studies/p1-gpr150-methods.md) · [采集工作流](../case_studies/data-acquisition-workflow.md) · [汇总数据](../assets/p1/p1-development-detail-summary.json)
