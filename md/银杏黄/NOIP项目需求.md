##NOIP项目需求列表

###客户端

	1>本地后台检出并提交
		1.1>检测目录内文件变化并提交[与服务端文件比较]
		1.2>由[服务器,客户端]设置自动提价时间(占据更小的系统资源)
		1.3>用户主动提交
	2>本地备份
		2.1>diff,无差异下不提交,直接生成新文件,不需要做差异备份
	3>断网与恢复检测
		3.1>物理机考试状态下断网,断网恢复时需检测,可采用与服务器握手
	4>log与错误恢复及反馈
		4.1>同时链接多个服务端
		4.2>本地插件从异常中恢复后:
			4.2.1>获取服务器最新信息及本地状态[维护一个list]
	5>服务端推送
		5.1>弹出服务端推送信息
		5.2>客户端完成事项与服务端对比,进行未完成事项
		5.3>命令推送[管理员权限]

###服务端
	
	1>基本配置->>[以竞赛名称为首目录]
		1.1>配置文件目录
		1.2>客户端生成器
			1.2.a>建议可配置服务器IP
			1.2.b>或扫描)
		1.3>log
		1.4>导入OIer信息,独立目录或单文件
		1.5>导入[可移植的]题目信息:题目目录,子目录
		1.6>备份及恢复[自动/手动]
		1.7>服务端和评测独占的系统资源*
			1.7.2>检测是否低于题目要求上限
	2>竞赛信息[独立的编辑界面]
		2.1>编辑比赛信息
		2.2>编辑OIer信息
		2.3>编辑题目信息
		2.4>编辑客户端配置
			2.4.1>填充本机IP
			2.4.2>定义下载网页路径
			2.4.3>定义题目下载路径
		2.5>编辑推送[是/否]
			2.5.1>信息推送开关
				2.5.1.1>时间提醒
			2.5.2>命令推送开关
	3>配置考试网络
		3.1>分发客户端及试题
		3.2>同步开题
			3.2.a>分发带密码的试题.zip,按服务器时间给key(可能需要客户端设置key界面)
			3.2.b>在线分发试题提供下载(服务端配置局域网文件下放)
		3.3>与客户端建立连接并保持信息
	4>收取选手源文件/压缩包
		4.1>最后一次校验(比赛结束时)
		4.2>收取选手文件:
			4.2.1>以选手唯一识别信息命名的所有题目源文件的压缩文件
			4.2.2>4.2.1中压缩文件的加密文件[参赛选手自定密码,用以成绩公示后申诉调阅代码]
				  ！此步骤要求参赛选手打包最后一次提交的代码！
	5>评测
		5.1>安全测试
			5.1.1>只允许调用规定的文件/函数,违规给出CE
				5.1.1.1>非法操作检测
			>>>这里可能需要独立/虚拟测试环境
			5.1.2>编译死循环检测
				>由于编译时间不在时间限制内,需判定编译是否陷入死循环
				5.1.2.a>编译时间过长却正常:编译时间上限不宜过小
				5.1.2.b>编译/预编译代码中对违规代码识别
		5.2>常规测试[各步骤同步,最终统一检测]
			5.2.1>在所有应当通过编译的文件编译好之后再统一进行评测
			5.2.2>控制台模式
				5.2.2.1>文件重定向
			5.2.3>文件模式
				5.2.3.1>比对文件
			5.2.5>测试截断
				5.2.5.1>超出题目条件限制给出错误信息:CE>RE,MLE,TLE>WA>PE>AC
			5.2.6>成绩与排名
				5.2.6>按成绩排名
				5.2.7>添加加权分数
				5.3.8>添加其他个人分数[可加权](拓展性需要求,可去?)
		5.3>独立测试
			5.3.1>在已连接客户端中直接测试指定用户指定题目
			5.3.2>独立选手分数测评
				5.3.2.1>实时分数与信息反馈
	6>结果输出
		6.1>按选中的项目输出xls成绩单
			
###例外需求
	1.本地判题:CCF或第三出题方给出的测试数据格式差异,导致用户导入数据时间成本增加
	1.ans>编写生成指定测试数据标准文件的脚本



###预设
	1.标准化数据测试文件格式:
		1.1>[questionName][1-n].in,[questionName][1-n].out文件
	2.对输出结果的校验
		2.1>不检测最后的多余换行[弱化需求,可能需要修正,为兼容linux/windows]
		2.2>进行文本严格比对(ASCII比对至最后非控制字符)



```lc4t.me FROM NOIP项目组```
```Version 0.1```