# 🧩 自闭症（ASD）智能筛查辅助系统

基于 **Streamlit + PyCaret** 的自闭症谱系障碍早期筛查辅助平台，覆盖 **幼儿 / 儿童 / 青少年 / 成人** 四类人群，支持 **在线单人预测** 与 **CSV 批量预测** 两种模式。使用者通过回答标准化筛查问卷（Q-CHAT-10 量表风格问题）与基本信息，系统即输出 ASD 风险预测结果。

> ⚠️ **免责声明**：本系统输出结果仅供筛查参考与学术研究使用，**不能替代专业医疗机构的诊断**。如有疑虑请前往正规医院就诊。

## ✨ 功能特性

- **四类人群全覆盖**：幼儿（Toddler）、儿童（Child）、青少年（Adolescent）、成人（Adult）独立建模
- **在线预测**：逐题回答 10 道自闭症筛查问题（Q-CHAT-10），附加年龄、性别、种族、黄疸史、家族 ASD 史等基本信息，实时输出预测
- **批量预测**：上传 CSV 数据，一次完成多人筛查，输出预测标签表格，适合机构初筛场景
- **图片识别模块**：预留自闭症相关图像识别入口（基于 PyTorch 模板扩展）
- **低代码模板架构**：基于 [traingenerator](https://github.com/jrieke/traingenerator) 的 Jinja 模板引擎，每个模块由 `code-template.py.jinja + sidebar.py + test-inputs.yml` 组成，易于扩展新人群/新问卷

## 🏗️ 系统架构

```
                    ┌────────────────────────────┐
                    │        main.py (Streamlit)  │
                    │   模板路由 / 页面框架 / UI    │
                    └──────────┬─────────────────┘
                               │
        ┌──────────────┬───────┴────────┬───────────────┐
        ▼              ▼                ▼               ▼
   1.幼儿模块      2.儿童模块       3.青少年模块      4.成人模块
  （在线/批处理）  （在线/批处理）   （在线/批处理）   （在线/批处理）
        │              │                │               │
        ▼              ▼                ▼               ▼
  autism-Toddler  autism-Child   autism-Adolescent  autism-Adult
   2021-7-28.pkl   2021-7-28.pkl    2021-7-28.pkl    2021-7-28.pkl
        └──────────────┴────────┬───────┴───────────────┘
                                ▼
                     PyCaret (predict_model)
                                ▼
                       ASD 风险预测（YES / NO）
```

## 📁 目录结构

```
Machine-learning-autism-monitoring-project/
├── main.py                     # Streamlit 应用入口（模板加载与路由）
├── utils.py                    # 模板渲染 / 代码生成辅助工具
├── templates/                  # 各人群 × 各模式的功能模块
│   ├── 1.幼儿_在线预测/        #   幼儿单人预测（Q-CHAT-10 + 周龄等）
│   ├── 1.幼儿_批处理预测/      #   幼儿 CSV 批量预测
│   ├── 2.儿童_在线预测/        #   儿童单人预测
│   ├── 2.儿童_批出理预测/      #   儿童 CSV 批量预测
│   ├── 3.青少年_在线预测/      #   青少年单人预测（含国家/年龄段等）
│   ├── 3.青少年_批处理预测/    #   青少年 CSV 批量预测
│   ├── 4.成人_在线预测/        #   成人单人预测
│   ├── 4.成人_批处理预测/      #   成人 CSV 批量预测
│   └── 自闭症图片识别/         #   图像识别模块（扩展用）
├── autism-Child-2021-7-28.pkl      # 儿童 PyCaret 分类模型
├── autism-Toddler2021-7-28.pkl     # 幼儿 PyCaret 分类模型
├── requirements.txt
└── setup.sh                    # Streamlit 一键配置脚本
```

每个模块目录包含：

| 文件 | 作用 |
|------|------|
| `sidebar.py` | 问卷表单 + 模型加载 + 预测逻辑 |
| `code-template.py.jinja` | 代码生成模板（traingenerator 风格） |
| `test-inputs.yml` | 模板测试输入配置 |

## 🚀 快速开始

### 环境要求

- Python 3.7
- 依赖：`pycaret==2.3.2`、`streamlit==0.85.0`、`pandas==1.2.4`、`numpy==1.19.5`

### 安装与运行

```bash
pip install -r requirements.txt

# 可选：初始化 Streamlit 配置
bash setup.sh

streamlit run main.py
```

浏览器打开 `http://localhost:8501`，选择对应人群与模式：

1. **在线预测** — 回答 10 道筛查问题（勾选 = 是）+ 填写基本信息 → 点击「预测」
2. **批处理预测** — 上传符合问卷字段格式的 CSV → 得到批量预测结果

### 问卷说明（以幼儿为例）

- **10 道筛查问题**（Q-CHAT-10 风格）：叫名字是否回应、眼神交流、用手指物、分享兴趣、假装游戏、跟随视线、安慰他人、第一句话、手势使用、无目的凝视等
- **基本信息**：周龄、性别、种族、是否有黄疸、是否有亲人患 ASD、测试完成者
- **输出**：`YES`（有潜在自闭症特征）/ `NO`（无自闭症特征）

## 🧠 模型说明

| 人群 | 模型文件 | 状态 |
|------|----------|------|
| 幼儿 Toddler | `autism-Toddler2021-7-28.pkl` | ✅ 已包含 |
| 儿童 Child | `autism-Child-2021-7-28.pkl` | ✅ 已包含 |
| 青少年 Adolescent | `autism-Adolescent-2021-7-28.pkl` | ⚠️ 需自行训练补充 |
| 成人 Adult | `autism-Adult2021-7-28.pkl` | ⚠️ 需自行训练补充 |

- 模型均使用 **PyCaret 2.3.2** 训练并序列化为 `.pkl`，通过 `load_model()` / `predict_model()` 调用
- 数据集基于公开的 ASD 筛查数据（UCI 风格：Toddler / Child / Adolescent / Adult 四份问卷数据）
- 补充模型：使用 PyCaret 训练后导出为对应命名的 `.pkl` 放在仓库根目录即可被各模块加载

## 🔧 扩展新模块

1. 在 `templates/` 下新建 `N.人群_模式/` 目录
2. 编写 `sidebar.py`（表单 + `load_model` + `predict_model`）
3. 配置 `code-template.py.jinja` 与 `test-inputs.yml`
4. `main.py` 会自动扫描 `templates/` 并注册新模块

## 🙏 致谢

- 模板框架基于 [jrieke/traingenerator](https://github.com/jrieke/traingenerator)
- 建模工具 [PyCaret](https://pycaret.org/)

## 📄 License

本仓库暂未指定开源许可证。
