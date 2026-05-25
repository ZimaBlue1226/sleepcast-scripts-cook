# SleepCast 用户画像 / Audience Profile

> 本文件描述 SleepCast 的目标听众与内容偏好，供 `sleepcast-script` skill 在每次生成选题和脚本时默认参考。
> 你可以自行增删改本文件，无需在每次使用 skill 时重复输入这些信息。
> 初始内容根据 VelaSleep 项目背景（project_context.md 第 2 节）填充。

## 1. 目标听众

- 地区：北美（首发核心市场）
- 年龄：24–45 岁成年人
- 共性：睡前容易高唤起（脑子停不下来），或已习惯使用睡眠内容入睡

## 2. 典型需求

- 睡前脑子停不下来，希望快速降唤醒
- 不想在睡前继续做复杂选择
- 已习惯睡眠故事、白噪音、冥想或声景内容
- 希望获得安全、温暖、低刺激、低屏幕负担的睡前陪伴
- 对 AI 健康/陪伴类产品有隐私顾虑，重视"不保存原始音频"等承诺

## 3. 内容偏好

- 原生英文、像 native sleep story / sleep podcast 的语感，而非翻译腔
- 约 30 分钟人声叙事 + 后续无人声背景音循环的结构
- 文学化、克制、具象、感官化的叙述；慢节奏、低信息密度
- 喜欢可长时间停留、无任务、无社交压力的安全场景
- 接受温暖、被照料、被守护的氛围（守护者角色可有可无、绝不打扰）

## 4. 体验红线（内容创作须遵守）

- 低刺激、慢节奏、低信息密度；避免惊吓、强剧情、任务感、屏幕刺激
- 避免医疗化语言，不做诊断/治疗承诺；定位是 sleep companion / guide / coach，不是 therapist
- 禁止出现：手机、屏幕、闹钟、具体时间数字、工作相关物件、现代电子设备、镜子、尖锐物品、突然的动物叫声
  （详细禁区以 `references/sleepcast_script_prompt.md` 为准）

## 5. 题材方向（可按测试结果迭代）

- 当前首轮 YouTube 测试优先方向：`Cozy Snow Cabin`、`Rainy Night Restoration Shop`
- `Rainy Night Restoration Shop` 与 Headspace 的 `Rainday Antiques` 接近，需强调差异化：
  restoration shop、旧物修复、照料、手工工具、音乐盒、金缮瓷碗等具体意象，而非泛泛的 antique shop
