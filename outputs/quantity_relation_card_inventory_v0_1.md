# Quantity Relation Card Inventory v0.1

## Summary

- total quantity relation cards: 65
- categories found: 22
- method cards found: 65
- source files checked: knowledge_base/all_cards.jsonl, knowledge_base/module_originals/quantity_relation/
- field availability: id, module, question_type, sub_type, method_name, tags, trigger_conditions, anti_conditions, required_inputs, reasoning_policy, calculation_policy, solver_priority, steps, formulas, examples, pitfalls, forbidden, output_constraints, source_file, source_page, confidence, need_review, source_zip

## Cards by category

### 数论与计算
- qr_calculation_formula_001 | 常用代数公式与乘方尾数法 | tags: 平方差, 完全平方, 立方和差, 尾数, 幂运算 | confidence=0.86 | need_review=True
- qr_number_property_001 | 倍数、整除与余数特性 | tags: 倍数, 整除, 最小公倍数, 最大公约数, 余数 | confidence=0.9 | need_review=False

### 余数问题
- qr_remainder_formula_001 | 余同取余、和同加和、差同减差 | tags: 余数, 口诀, 最小公倍数, 周期 | confidence=0.94 | need_review=False
- qr_remainder_enum_001 | LCM*n+x枚举法 | tags: 余数, 枚举, 最小公倍数 | confidence=0.93 | need_review=False

### 数列问题
- qr_sequence_formula_001 | 等差、等比与递推数列公式 | tags: 等差数列, 等比数列, 斐波那契, 求和, 归纳 | confidence=0.92 | need_review=False

### 数字推理
- qr_numeric_reasoning_001 | 差商幂修正与分组观察法 | confidence=0.88 | need_review=False

### 平均数问题
- qr_average_number_001 | 等距离/等时间平均速度及A=B*C迁移 | confidence=0.95 | need_review=False

### 方程问题
- qr_equation_method_001 | 和差倍比与问什么设什么 | confidence=0.88 | need_review=False

### 不定方程
- qr_indeterminate_equation_001 | 奇偶、整除、代入、消元与赋零法 | confidence=0.92 | need_review=False

### 浓度/溶液混合问题
- qr_concentration_basic_001 | 浓度基础公式与溶质守恒 | confidence=0.94 | need_review=False
- qr_alligation_001 | 已知3个浓度求两部分量之比 | confidence=0.95 | need_review=False

### 容斥/集合问题
- qr_inclusion_exclusion_001 | 圈内圈外与人次重复关系 | confidence=0.95 | need_review=False
- qr_inclusion_exclusion_extreme_001 | 反向构造相交最小/最大 | confidence=0.9 | need_review=False

### 牛吃草问题
- qr_cow_grazing_001 | 白吃牛与干活牛三步法 | confidence=0.94 | need_review=False

### 周期循环问题
- qr_cycle_mod_001 | 去掉完整周期看余数 | confidence=0.96 | need_review=False

### 日期星期问题
- qr_date_week_001 | 粗算修正日期差法 | confidence=0.95 | need_review=False

### 年龄问题
- qr_age_problem_001 | 年龄差与现实范围切入法 | confidence=0.92 | need_review=False

### 工程问题
- qr_work_basic_001 | 工作总量=效率×时间与赋值法 | confidence=0.96 | need_review=False
- qr_work_rest_001 | 休息意味着另一人继续工作 | confidence=0.92 | need_review=False

### 经济利润问题
- qr_profit_basic_001 | 成本、售价、利润率基础公式 | confidence=0.96 | need_review=False
- qr_profit_batch_001 | 按各批收入相加列总收入方程 | confidence=0.92 | need_review=False
- qr_profit_fund_flow_001 | 只看应收回金额不看过程 | confidence=0.9 | need_review=False

### 统筹规划问题
- qr_planning_optimal_001 | 工程/运输/经济统筹的低耗优先法 | confidence=0.88 | need_review=False
- qr_time_planning_001 | 等待时间最少与煎饼共用时间 | confidence=0.82 | need_review=False
- qr_balance_weighing_001 | 接近3^n判断称重次数 | confidence=0.78 | need_review=True
- qr_bottle_exchange_001 | n瓶换1瓶转化为n-1个空瓶换无瓶酒 | confidence=0.84 | need_review=False

### 最值问题
- qr_extreme_sum_fixed_001 | 总和固定下问某部分最多/最少 | confidence=0.95 | need_review=False
- qr_extreme_unfavorable_001 | 构造最不利保证n人满足 | confidence=0.95 | need_review=False
- qr_extreme_function_001 | 二次函数顶点与均值定理 | confidence=0.94 | need_review=False
- qr_extreme_product_001 | 总平均固定下的十字相乘极值 | confidence=0.9 | need_review=False
- qr_extreme_three_end_001 | 两端同向极端构造 | confidence=0.9 | need_review=False

### 排列组合
- qr_perm_comb_basic_001 | 有序为排列、无序为组合，分类加法分步乘法 | confidence=0.96 | need_review=False
- qr_adjacent_bundle_001 | 捆绑法 | confidence=0.95 | need_review=False
- qr_nonadjacent_insert_001 | 插空法 | confidence=0.95 | need_review=False
- qr_fixed_order_001 | 全排列除以特定元素全排列 | confidence=0.88 | need_review=False
- qr_same_elements_distribution_001 | 插板法 | confidence=0.96 | need_review=False
- qr_average_grouping_001 | 无序除堆排序，有序直接选 | confidence=0.95 | need_review=False
- qr_derangement_001 | 记忆1-6元素错排数 | confidence=0.96 | need_review=False
- qr_circular_permutation_001 | 环形固定一位后排列 | confidence=0.94 | need_review=False
- qr_repeated_permutation_001 | 每位独立选择n^m | confidence=0.94 | need_review=False

### 概率问题
- qr_probability_basic_001 | 符合情况/所有可能情况 | confidence=0.95 | need_review=False
- qr_geometric_probability_001 | 长度/面积/体积比求概率 | confidence=0.92 | need_review=False
- qr_two_person_same_group_001 | 先固定一人再看另一人 | confidence=0.96 | need_review=False
- qr_lottery_probability_001 | 先抽后抽概率相同 | confidence=0.92 | need_review=False
- qr_match_probability_order_001 | 负场位置限制 | confidence=0.9 | need_review=False

### 几何问题
- qr_geometry_formula_001 | 常用长度、面积、体积公式 | confidence=0.95 | need_review=False
- qr_geometry_scaling_001 | 边长、面积、体积倍数关系 | confidence=0.96 | need_review=False
- qr_geometry_extreme_001 | 越接近圆/球极值越优 | confidence=0.94 | need_review=False
- qr_shortest_distance_001 | 对称展开与垂线最短 | confidence=0.94 | need_review=False
- qr_one_stroke_001 | 一笔画奇点规则 | confidence=0.88 | need_review=False

### 行程问题
- qr_travel_basic_001 | 路程=速度×时间与比例法 | confidence=0.96 | need_review=False
- qr_meeting_chasing_001 | 速度和/速度差公式 | confidence=0.96 | need_review=False
- qr_multiple_meeting_001 | 第N次相遇走2N-1个全程 | confidence=0.91 | need_review=False
- qr_circular_motion_001 | 同起点同向追及/背向相遇 | confidence=0.92 | need_review=False
- qr_stream_boat_001 | 船速水速顺逆公式 | confidence=0.94 | need_review=False
- qr_escalator_001 | 变形行船模型 | confidence=0.88 | need_review=False
- qr_train_bridge_001 | 车身长不可忽略 | confidence=0.94 | need_review=False
- qr_team_marching_001 | 队头到队尾的相对速度 | confidence=0.88 | need_review=False

### 特殊情景应用
- qr_chicken_rabbit_001 | 理论最大值与实际值差值公式 | confidence=0.95 | need_review=False
- qr_surplus_deficit_001 | 盈数亏数除以分配标准差 | confidence=0.95 | need_review=False
- qr_square_array_001 | 最外层边长平方与层人数公式 | confidence=0.94 | need_review=False
- qr_tree_planting_001 | 两端/一端/环形/两端不植树公式 | confidence=0.96 | need_review=False
- qr_tree_overlap_001 | 两次植树最大公约数求无需移动棵数 | confidence=0.86 | need_review=False
- qr_clock_problem_001 | 时针分针追及模型 | confidence=0.94 | need_review=False

### 比赛问题
- qr_competition_schedule_001 | 循环赛、淘汰赛与轮空规则 | confidence=0.95 | need_review=False

## Cards by method

### 代入排除
- qr_number_property_001 | 倍数、整除与余数特性 | reasoning_policy: option_filter_first
- qr_indeterminate_equation_001 | 奇偶、整除、代入、消元与赋零法 | reasoning_policy: enumeration

### 特值法
- qr_work_basic_001 | 工作总量=效率×时间与赋值法 | reasoning_policy: formula_then_filter (赋值法)
- qr_profit_basic_001 | 成本、售价、利润率基础公式 | reasoning_policy: formula_then_filter

### 方程法
- qr_equation_method_001 | 和差倍比与问什么设什么 | reasoning_policy: formula_then_filter
- qr_profit_batch_001 | 按各批收入相加列总收入方程 | reasoning_policy: formula_then_filter

### 赋值法
- qr_work_basic_001 | 工作总量=效率×时间与赋值法 | reasoning_policy: formula_then_filter

### 枚举法
- qr_remainder_enum_001 | LCM*n+x枚举法 | reasoning_policy: enumeration
- qr_indeterminate_equation_001 | 奇偶、整除、代入、消元与赋零法 | reasoning_policy: enumeration

### 十字交叉法
- qr_alligation_001 | 已知3个浓度求两部分量之比 | reasoning_policy: formula_then_filter
- qr_extreme_product_001 | 总平均固定下的十字相乘极值 | reasoning_policy: formula_then_filter

### 比例法
- qr_travel_basic_001 | 路程=速度×时间与比例法 | reasoning_policy: formula_then_filter
- qr_meeting_chasing_001 | 速度和/速度差公式 | reasoning_policy: formula_then_filter
- qr_average_number_001 | 等距离/等时间平均速度及A=B*C迁移 | reasoning_policy: formula_then_filter

### 图表辅助
- qr_inclusion_exclusion_001 | 圈内圈外与人次重复关系 | reasoning_policy: formula_then_filter (圈图)
- qr_geometry_formula_001 | 常用长度、面积、体积公式 | reasoning_policy: formula_then_filter

### 公式/口诀
- qr_calculation_formula_001 | 常用代数公式与乘方尾数法 | reasoning_policy: shortcut_first
- qr_remainder_formula_001 | 余同取余、和同加和、差同减差 | reasoning_policy: formula_then_filter
- qr_sequence_formula_001 | 等差、等比与递推数列公式 | reasoning_policy: pattern_first
- qr_concentration_basic_001 | 浓度基础公式与溶质守恒 | reasoning_policy: formula_then_filter
- qr_cow_grazing_001 | 白吃牛与干活牛三步法 | reasoning_policy: formula_then_filter
- qr_chicken_rabbit_001 | 理论最大值与实际值差值公式 | reasoning_policy: formula_then_filter
- qr_perm_comb_basic_001 | 有序为排列、无序为组合 | reasoning_policy: formula_then_filter
- qr_derangement_001 | 记忆1-6元素错排数 | reasoning_policy: formula_then_filter

### 模型/套路
- qr_stream_boat_001 | 船速水速顺逆公式 | reasoning_policy: formula_then_filter
- qr_train_bridge_001 | 车身长不可忽略 | reasoning_policy: formula_then_filter
- qr_multiple_meeting_001 | 第N次相遇走2N-1个全程 | reasoning_policy: formula_then_filter
- qr_circular_motion_001 | 同起点同向追及/背向相遇 | reasoning_policy: formula_then_filter
- qr_escalator_001 | 变形行船模型 | reasoning_policy: formula_then_filter
- qr_team_marching_001 | 队头到队尾的相对速度 | reasoning_policy: formula_then_filter
- qr_clock_problem_001 | 时针分针追及模型 | reasoning_policy: formula_then_filter
- qr_tree_planting_001 | 两端/一端/环形/两端不植树公式 | reasoning_policy: formula_then_filter
- qr_tree_overlap_001 | 两次植树最大公约数求无需移动棵数 | reasoning_policy: formula_then_filter
- qr_square_array_001 | 最外层边长平方与层人数公式 | reasoning_policy: formula_then_filter
- qr_bottle_exchange_001 | n瓶换1瓶转化为n-1个空瓶换无瓶酒 | reasoning_policy: formula_then_filter
- qr_balance_weighing_001 | 接近3^n判断称重次数 | reasoning_policy: formula_then_filter
- qr_competition_schedule_001 | 循环赛、淘汰赛与轮空规则 | reasoning_policy: formula_then_filter

### 构造/极端
- qr_extreme_sum_fixed_001 | 总和固定下问某部分最多/最少 | reasoning_policy: formula_then_filter
- qr_extreme_unfavorable_001 | 构造最不利保证n人满足 | reasoning_policy: formula_then_filter
- qr_extreme_function_001 | 二次函数顶点与均值定理 | reasoning_policy: formula_then_filter
- qr_extreme_three_end_001 | 两端同向极端构造 | reasoning_policy: formula_then_filter
- qr_inclusion_exclusion_extreme_001 | 反向构造相交最小/最大 | reasoning_policy: formula_then_filter
- qr_geometry_extreme_001 | 越接近圆/球极值越优 | reasoning_policy: formula_then_filter
- qr_shortest_distance_001 | 对称展开与垂线最短 | reasoning_policy: formula_then_filter

### 统筹
- qr_planning_optimal_001 | 工程/运输/经济统筹的低耗优先法 | reasoning_policy: enumeration
- qr_time_planning_001 | 等待时间最少与煎饼共用时间 | reasoning_policy: enumeration

### 其他方法
- qr_surplus_deficit_001 | 盈数亏数除以分配标准差 | reasoning_policy: formula_then_filter
- qr_date_week_001 | 粗算修正日期差法 | reasoning_policy: formula_then_filter
- qr_age_problem_001 | 年龄差与现实范围切入法 | reasoning_policy: formula_then_filter
- qr_cycle_mod_001 | 去掉完整周期看余数 | reasoning_policy: formula_then_filter
- qr_one_stroke_001 | 一笔画奇点规则 | reasoning_policy: formula_then_filter
- qr_numeric_reasoning_001 | 差商幂修正与分组观察法 | reasoning_policy: pattern_first
- qr_work_rest_001 | 休息意味着另一人继续工作 | reasoning_policy: formula_then_filter
- qr_profit_fund_flow_001 | 只看应收回金额不看过程 | reasoning_policy: formula_then_filter
- qr_adjacent_bundle_001 | 捆绑法 | reasoning_policy: formula_then_filter
- qr_nonadjacent_insert_001 | 插空法 | reasoning_policy: formula_then_filter
- qr_fixed_order_001 | 全排列除以特定元素全排列 | reasoning_policy: formula_then_filter
- qr_same_elements_distribution_001 | 插板法 | reasoning_policy: formula_then_filter
- qr_average_grouping_001 | 无序除堆排序，有序直接选 | reasoning_policy: formula_then_filter
- qr_circular_permutation_001 | 环形固定一位后排列 | reasoning_policy: formula_then_filter
- qr_repeated_permutation_001 | 每位独立选择n^m | reasoning_policy: formula_then_filter
- qr_probability_basic_001 | 符合情况/所有可能情况 | reasoning_policy: formula_then_filter
- qr_geometric_probability_001 | 长度/面积/体积比求概率 | reasoning_policy: formula_then_filter
- qr_two_person_same_group_001 | 先固定一人再看另一人 | reasoning_policy: formula_then_filter
- qr_lottery_probability_001 | 先抽后抽概率相同 | reasoning_policy: formula_then_filter
- qr_match_probability_order_001 | 负场位置限制 | reasoning_policy: formula_then_filter
- qr_geometry_scaling_001 | 边长、面积、体积倍数关系 | reasoning_policy: formula_then_filter

## Notes

- 字段缺失情况：所有 65 张卡片字段完整，包含 id, module, question_type, sub_type, method_name, tags, trigger_conditions, anti_conditions, required_inputs, reasoning_policy, calculation_policy, solver_priority, steps, formulas, examples, pitfalls, forbidden, output_constraints, source_file, source_page, confidence, need_review, source_zip。
- 多类别归属：部分卡片的方法可能跨类别（如代入排除法同时用于不定方程和整除问题），但 question_type 分类清晰。
- 题型类与方法类的重叠：question_type 按题型分类（22 类），method_name 按解题方法分类（65 种），两者有交叉但维度不同。
- 不确定归类：qr_balance_weighing_001（天平称重）confidence=0.78 偏低，归入统筹规划问题但可能更适合归入最值问题。
- need_review=True 的卡片：qr_calculation_formula_001（confidence=0.86）和 qr_balance_weighing_001（confidence=0.78）需要人工复核。
