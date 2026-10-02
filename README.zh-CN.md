# 赛车数据分析与车辆工程作品集

[English](README.md) · 中文

我是香港中文大学（深圳）的计算机科学学生。我自己骑车、采集数据并完成分析，也参与模拟赛车练习和比赛，开发车辆动力学与圈速计算工具。

这里收录了我在实车和模拟赛车中的工作：整理遥测与影像，比较线路和控制动作，定位时间损失，制定驾驶或设定对照，以及构建车辆模型。

![aprilia GPR150 在 P1 的赛道照片](assets/p1/p1-field-photo-panels.png)

## 项目入口

1. **[aprilia GPR150 / P1 实车数据分析](zh/aprilia-gpr150-p1.md)**：九节练习、71 个计时圈；刹车参照的演变、开油时机、连续弯线路与圈速收益。
2. **[模拟赛车分析与测试](zh/sim-racing.md)**：MX-5、F4、GT1；回放与遥测整合、轮载与抱死分析、比赛损失和设定测试。
3. **[车辆动力学与最小圈速建模](zh/vehicle-modelling.md)**：CBR650R 的台架曲线、车辆参数、赛道几何、附着情景、线路与速度计算。
4. **[CBR650R / 赛道日练习分析](case_studies/hualong-cbr650r.md)**：四节实车练习；油门归一化、可比圈筛选与出弯动作复盘。英文案例。
5. **[实车采集与现场工作流](case_studies/data-acquisition-workflow.md)**：RaceChrono、GPS／IMU／胸部心率带、BLE OBD、头盔影像和 Circuit Tools 3。英文说明。

## 我能为车队做什么

| 车队任务 | 已有工作证据（Evidence from the work） |
|---|---|
| 整理节次数据 | [实车采集工作流](case_studies/data-acquisition-workflow.md)：记录 GNSS／IMU／OBD 与影像，检查时钟、定位质量和圈边界；[模拟赛车分析](zh/sim-racing.md)：整合回放与遥测，恢复缺失通道。 |
| 定位性能损失 | [GPR150 / P1](zh/aprilia-gpr150-p1.md)：按地理分段追踪连续弯收益与损失；[MX-5 / Lime Rock](case_studies/lime-rock-mx5-race-analysis.md)：S1 占排位差距的 60.5%，七段主要慢速区间合计损失 28.50 s。 |
| 将车辆数据转成测试方案 | [F4 / Paul Ricard](case_studies/paul-ricard-f4-development.md)：对照刹车释放、出弯速度与后轮轮载；[GT1 / Silverstone](case_studies/silverstone-gt1-sim.md)：定位前轮抱死区间，提出前刹车配比 61% → 60.5% 的单变量测试。 |
| 复盘圈速稳定性 | [GPR150 / P1](zh/aprilia-gpr150-p1.md)：九节练习、71 个计时圈，比较刹车参照演变与连续圈；[三场模拟比赛](case_studies/paul-ricard-race-consistency.md)：用中位数、MAD、损伤与切弯记录比较代表圈速和事故恢复损失。 |
| 支持实车采集与节间复盘 | [采集与现场工作流](case_studies/data-acquisition-workflow.md)：RaceChrono、GPS／IMU／胸部心率带、vLinker MC+ BLE OBD、Action 5 Pro 头盔影像与多机位对齐；休息期间在 P 房用 Circuit Tools 3 复盘并制定下一节计划。 |
| 开发模型与分析工具 | [CBR650R / P1 建模](zh/vehicle-modelling.md)：整合实测数据、台架曲线、传动比与赛道几何，计算附着包络、线路、速度和挡位；提供[可运行的圈速计算代码](modelling/code/README.md)。 |

[技术栈与实现](TECHNICAL_PROFILE.md) · [节间复盘与练习记录](TRACKSIDE_FEEDBACK_LOOP.md) · [工程工作概览](PORTFOLIO.md)

中文页面提供项目概述；各页可直接进入详细分析、方法、数据和代码。
