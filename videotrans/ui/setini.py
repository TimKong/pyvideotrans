# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setini.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
from pathlib import Path

from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QFileDialog

from videotrans.configure import config


class Ui_setini(object):
    def get_target(self, btn):
        dirname = QFileDialog.getExistingDirectory(self, config.transobj['selectsavedir'], Path.home().as_posix())
        if dirname:
            dirpath = Path(dirname)
            config.HOME_DIR = dirpath.as_posix()
            config.TEMP_HOME = config.HOME_DIR + '/tmp'
            config.settings['homedir'] = config.HOME_DIR
            btn.setText(config.HOME_DIR)
            Path(config.TEMP_HOME).mkdir(parents=True, exist_ok=True)
            json.dump(config.settings, open(config.ROOT_DIR + "/videotrans/cfg.json", 'w', encoding='utf-8'),
                      ensure_ascii=False)

    def setupUi(self, setini):
        setini.setObjectName("setini")
        setini.setWindowModality(QtCore.Qt.NonModal)
        setini.resize(900, 670)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(setini.sizePolicy().hasHeightForWidth())
        setini.setSizePolicy(sizePolicy)

        self.verticalLayoutWidget = QtWidgets.QWidget(setini)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 860, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")

        scroll_area = QtWidgets.QScrollArea(setini)
        scroll_area.setWidgetResizable(True)
        scroll_area.setAlignment(Qt.AlignmentFlag.AlignTop)

        box = QtWidgets.QWidget()  # 创建新的 QWidget，它将承载你的 QHBoxLayouts
        box.setLayout(QtWidgets.QVBoxLayout())

        # 中文注释 界面ui控制
        self.notices = {
            "common": {
                "lang": "设置软件界面语言，修改后需要重启软件",
                "countdown_sec": "当单个视频翻译时，暂停时倒计时秒数",
                "backaudio_volume": "背景音频音量值为原本的倍数",
                "loop_backaudio": "如果背景音频时长短于视频，是否重复播放背景音，默认否",
                "bgm_split_time": "设置分离背景音时切割片段，防止视频过长卡死，默认300s",
                "homedir": "家目录，用于保存视频分离、字幕配音、字幕翻译等结果的位置，默认用户家目录"
            },
            "model": {
                "ai302_models": "填写302.ai用于翻译的模型名字，以英文逗号分隔",
                "ai302tts_models": "填写302.ai用于配音的模型名字，以英文逗号分隔",
                "chatgpt_model": "可供选择的chatGPT模型，以英文逗号分隔",
                "openaitts_model": "可供选择的OpenAI TTS模型，以英文逗号分隔",
                "openairecognapi_model": "OpenAI语音识别可供选择的模型，目前仅支持whisper-1",
                "gemini_model": "Gemini模型列表，以英文逗号分隔",
                "azure_model": "可供选择的模型，以英文逗号分隔",
                "localllm_model": "可供选择的模型，以英文逗号分隔",
                "zijiehuoshan_model": "填写在字节火山方舟创建的推理接入点名称 创建方法见 https://pyvideotrans.com/zijiehuoshan"
            },
            "video": {
                "crf": "视频转码时损失控制，0=损失最低，51=损失最大，默认13",
                "cuda_qp": "在 NVIDIA cuda上是否使用 qp代替crf，true=是，false=否",
                "preset": "用于控制输出视频质量和大小，越快质量越差",
                "ffmpeg_cmd": "自定义ffmpeg命令参数， 将添加在倒数第二个位置上,例如  -bf 7 -b_ref_mode middle",
                "video_codec": "采用 libx264 编码或 libx265编码，264兼容性更好，265压缩比更大清晰度更高"
            },
            "justify": {
                "audio_rate": "音频最大加速倍数，默认3，即最大加速到 3倍速度，需设置1-100的数字，比如3，代表最大加速3倍",
                "video_rate": "视频慢速倍数：大于1的数，代表最大允许慢速多少倍，0或1代表不进行视频慢放",
                "remove_silence": "是否移除配音末尾空白，true=移除，false=不移除",
                "remove_srt_silence": "是否移除原始字幕时长大于配音时长 的静音，比如原时长5s，配音后3s，是否移除这2s静音，true=移除，false=不移除",
                "remove_white_ms": "移除2条字幕间的静音长度ms，比如100ms，即如果两条字幕间的间隔大于100ms时，将移除100ms, -1=完全移除",
                "force_edit_srt": "true=强制修改字幕时间轴以便匹配声音，false=不修改，保持原始字幕时间轴，不修改可能导致字幕和声音不匹配"
            },
            "recogn": {
                "vad": "faster-whisper字幕整体识别模式时启用VAD",
                "overall_threshold": "VAD阈值",
                "overall_speech_pad_ms": "VAD pad值",
                "overall_silence": "最小静音片段ms，默认250ms ",
                "overall_maxsecs": "语句最大持续秒数",
                "voice_silence": "均等分割模式下静音片段",
                "interval_split": "均等分割模式下每个片段时长秒数"
            },
            "whisper": {
                "model_list": "faster模式和openai模式下的模型名字列表，英文逗号分隔",
                "cuda_com_type": "faster模式时cuda数据类型，int8=消耗资源少，速度快，精度低，float32=消耗资源多，速度慢，精度高，int8_float16=设备自选",
                "initial_prompt_zh": "发送给whisper模型的提示词",
                "whisper_threads": "faster模式下，字幕识别时，cpu进程数",
                "whisper_worker": "faster模式下，字幕识别时，同时工作进程数",
                "beam_size": "字幕识别时精度调整，1-5，1=消耗显存最低，5=消耗显存最多",
                "best_of": "字幕识别时精度调整，1-5，1=消耗显存最低，5=消耗显存最多",
                "temperature": "0=占用更少GPU资源但效果略差，1=占用更多GPU资源同时效果更好",
                "condition_on_previous_text": "true=占用更多GPU效果更好，false=占用更少GPU效果略差",
                "zh_hant_s": "强制将识别出的繁体字幕转为简体"
            },
            "subtitle": {
                "fontsize": "硬字幕字体像素尺寸",
                "fontname": "硬字幕时字体名字",
                "fontcolor": "设置字体的颜色，注意&H后的6个字符，每2个字母分别代表 BGR 颜色，即2位蓝色/2位绿色/2位红色，同同时常见的RGB色色颠倒的。",
                "fontbordercolor": "设置字体边框颜色，注意&H后的6个字符，每2个字母分别代表 BGR 颜色，即2位蓝色/2位绿色/2位红色，同同时常见的RGB色色颠倒的。",
                "subtitle_bottom": "字幕默认位于视频底部，此处可设置大于0的数值，代表字幕上移多少距离，注意最大不可大于(视频高度-20),也就是要保留至少20的高度用于显示字幕，否则字幕将不可见",
                "cjk_len": "中日韩硬字幕时一行长度字符个数，多于这个将换行",
                "other_len": "其他语言硬字幕时换行长度，多于这个字符数量将换行",
            },
            "trans": {
                "trans_thread": "同时翻译的字幕条数",
                "retries": "翻译出错时的重试次数",
                "translation_wait": "每次翻译后暂停时间/秒,用于限制请求频率",

            },
            "dubbing": {
                "dubbing_thread": "同时配音的字幕条数",
                "azure_lines": "azureTTS一次配音行数",
                "chattts_voice": "chatTTS 音色值"
            }
        }
        # 中文左侧label
        self.titles = {
            "ai302_models": "302.ai翻译模型列表",
            "ai302tts_models": "302.aiTTS模型列表",
            "openairecognapi_model": "OpenAI语音识别模型",
            "homedir": "设置家目录",
            "lang": "界面语言",
            "crf": "视频转码损失控制",
            "cuda_qp": "NVIDIA使用qp代替crf",
            "preset": "输出视频质量控制",
            "ffmpeg_cmd": "自定义ffmpeg命令参数",
            "video_codec": "264或265视频编码",
            "chatgpt_model": "ChatGPT模型列表",
            "openaitts_model": "OpenAI TTS模型列表",
            "azure_model": "Azure模型列表",
            "localllm_model": "本地LLM模型列表",
            "zijiehuoshan_model": "字节火山推理接入点",
            "model_list": "faster和openai的模型列表",
            "audio_rate": "音频最大加速倍数",
            "video_rate": "视频慢速倍数",
            "remove_silence": "移除配音末尾空白",
            "remove_srt_silence": "移除字幕时长大于配音时长",
            "remove_white_ms": "移除2条字幕间的静音长度",
            "force_edit_srt": "强制修改字幕时间轴",
            "bgm_split_time": "背景音分离切割片段/s",
            "vad": "启用VAD",
            "overall_silence": "最小静音片段/ms",
            "overall_maxsecs": "语句最大持续秒数/s",
            "overall_threshold": "VAD阈值",
            "overall_speech_pad_ms": "VAD pad 值",
            "voice_silence": "均等分割时静音片段/ms",
            "interval_split": "均等分割时片段时长/s",
            "trans_thread": "同时翻译的字幕数",
            "retries": "翻译出错重试数",
            "dubbing_thread": "同时配音字幕数",
            "countdown_sec": "暂停倒计时/s",
            "backaudio_volume": "背景音量倍数",
            "loop_backaudio": "循环播放背景音",
            "cuda_com_type": "CUDA数据类型",
            "initial_prompt_zh": "whisper模型提示词",
            "whisper_threads": "faster-whisper cpu进程",
            "whisper_worker": "faster-whisper工作进程",
            "beam_size": "字幕识别准确度控制1",
            "best_of": "字幕识别准确度控制2",
            "temperature": "faster-whisper温度控制",
            "condition_on_previous_text": "上下文感知",
            "fontsize": "硬字幕字体像素",
            "fontname": "硬字幕字体名字",
            "fontcolor": "硬字幕文字颜色",
            "fontbordercolor": "硬字幕文字边框颜色",
            "subtitle_bottom": "硬字幕上移距离",
            "cjk_len": "中日韩硬字幕一行字符数",
            "other_len": "其他语言硬字幕行字符数",
            "zh_hant_s": "字幕繁体转为简体",
            "azure_lines": "AzureTTS批量行数",
            "chattts_voice": "ChatTTS音色值",
            "translation_wait": "翻译后暂停时间/s",
            "gemini_model": "Gemini模型列表"
        }
        # 中文分区
        self.heads = {
            "common": "通用设置",
            "model": "AI模型列表",
            "video": "视频输出",
            "recogn": "VAD参数",
            "whisper": "faster/openai模式调整",
            "justify": "字幕声音对齐",
            "subtitle": "硬字幕样式",
            "trans": "字幕翻译调整",
            "dubbing": "配音调整"
        }
        if config.defaulelang != 'zh':
            self.notices = {
                "common": {
                    "lang": "Set the software interface language, a restart is required after modification",
                    "countdown_sec": "Countdown seconds when pausing during single video translation",
                    "backaudio_volume": "Background audio volume multiplier of the original value",
                    "loop_backaudio": "Whether to loop background audio if its duration is shorter than the video, default is no",
                    "bgm_split_time": "Set the segment length for splitting background audio to prevent freezing on long videos, default is 300s",
                    "homedir": "Home directory, used to save the results of video separation, subtitle dubbing, subtitle translation, etc. Default user home directory"
                },
                "model": {
                    "ai302_models": "Specify the model names for translation used by 302.ai, separated by commas",
                    "ai302tts_models": "Specify the model names for dubbing used by 302.ai, separated by commas",
                    "chatgpt_model": "Available chatGPT models, separated by commas",
                    "openaitts_model": "Optional OpenAI TTS models, separated by English commas",
                    "openairecognapi_model": "OpenAI Speech to Text model, whisper-1",
                    "gemini_model": "Gemini model list, separated by commas",
                    "azure_model": "Available models, separated by commas",
                    "localllm_model": "Available models, separated by commas",
                    "zijiehuoshan_model": "Specify the inference access point name created in ByteDance HuoShan Ark, see https://pyvideotrans.com/zijiehuoshan for instructions"
                },
                "video": {
                    "crf": "Loss control during video transcoding, 0 = minimum loss, 51 = maximum loss, default is 13",
                    "cuda_qp": "Whether to use qp instead of crf on NVIDIA cuda, true = yes, false = no",
                    "preset": "Controls output video quality and size, the faster, the worse the quality",
                    "ffmpeg_cmd": "Custom ffmpeg command parameters, added at the penultimate position, e.g., -bf 7 -b_ref_mode middle",
                    "video_codec": "Use libx264 or libx265 encoding, 264 has better compatibility, 265 has higher compression ratio and clarity"
                },
                "justify": {
                    "audio_rate": "Maximum audio speed multiplier, default is 3, which means a maximum speed of 3 times, should be a number between 1 and 100, e.g., 3 represents a maximum speed of 3 times",
                    "video_rate": "Video slow motion multiplier: a number greater than 1 represents the maximum allowable slow motion, 0 or 1 means no slow motion",
                    "remove_silence": "Whether to remove silence at the end of the dubbing, true = remove, false = do not remove",
                    "remove_srt_silence": "Whether to remove silence when the original subtitle duration is longer than the dubbing duration, e.g., the original duration is 5s, and the dubbing is 3s, should the 2s silence be removed, true = remove, false = do not remove",
                    "remove_white_ms": "Silence length in ms between two subtitles to be removed, e.g., 100ms, if the interval between two subtitles is greater than 100ms, 100ms will be removed, -1 = remove completely",
                    "force_edit_srt": "true = force subtitle timeline adjustment to match the audio, false = do not adjust, keep the original subtitle timeline, no adjustment may cause subtitles and audio to be out of sync"
                },
                "recogn": {
                    "vad": "Enable VAD in faster-whisper overall subtitle recognition mode",
                    "overall_threshold": "VAD threshold",
                    "overall_speech_pad_ms": "VAD pad value",
                    "overall_silence": "Minimum silence segment in ms, default is 250ms",
                    "overall_maxsecs": "Maximum duration of a sentence in seconds",
                    "voice_silence": "Silence segment in equal split mode",
                    "interval_split": "Segment duration in seconds in equal split mode"
                },
                "whisper": {
                    "model_list": "Model names list for faster mode and openai mode, separated by commas",
                    "cuda_com_type": "Data type for cuda in faster mode, int8 = less resource usage, faster speed, lower precision, float32 = more resource usage, slower speed, higher precision, int8_float16 = device auto-select",
                    "initial_prompt_zh": "Prompt sent to the whisper model",
                    "whisper_threads": "Number of CPU processes for subtitle recognition in faster mode",
                    "whisper_worker": "Number of concurrent workers for subtitle recognition in faster mode",
                    "beam_size": "Precision adjustment during subtitle recognition, 1-5, 1 = lowest memory usage, 5 = highest memory usage",
                    "best_of": "Precision adjustment during subtitle recognition, 1-5, 1 = lowest memory usage, 5 = highest memory usage",
                    "temperature": "0 = less GPU resource usage but slightly worse performance, 1 = more GPU resource usage and better performance",
                    "condition_on_previous_text": "true = more GPU usage and better performance, false = less GPU usage but slightly worse performance",
                    "zh_hant_s": "Force conversion of recognized traditional Chinese subtitles to simplified Chinese"
                },
                "subtitle": {
                    "fontsize": "Pixel size of the hard subtitle font",
                    "fontname": "Font name for hard subtitles",
                    "fontcolor": "Set the font color, note the 6 characters after &H, each 2 characters represent the BGR color, i.e., 2 blue, 2 green, 2 red, in reverse of the common RGB color.",
                    "fontbordercolor": "Set the font border color, note the 6 characters after &H, each 2 characters represent the BGR color, i.e., 2 blue, 2 green, 2 red, in reverse of the common RGB color.",
                    "subtitle_bottom": "Subtitles are by default located at the bottom of the video, here you can set a value greater than 0, representing how much the subtitles should move up, note that the maximum value should not exceed (video height - 20), at least 20 height must be reserved for subtitles, otherwise the subtitles will not be visible",
                    "cjk_len": "Number of characters per line for CJK hard subtitles, will wrap if exceeding this length",
                    "other_len": "Wrap length for other languages' hard subtitles, will wrap if exceeding this number of characters"
                },
                "trans": {
                    "trans_thread": "Number of subtitles translated simultaneously",
                    "retries": "Number of retries when translation fails",
                    "translation_wait": "Pause time in seconds after each translation, used to limit request frequency"
                },
                "dubbing": {
                    "dubbing_thread": "Number of subtitles dubbed simultaneously",
                    "azure_lines": "Number of lines dubbed at once by azureTTS",
                    "chattts_voice": "chatTTS voice tone"
                }
            }

            self.heads = {
                "common": "General Settings",
                "model": "AI Model List",
                "video": "Video Output",
                "recogn": "VAD Parameters",
                "whisper": "faster/openai Adjustments",
                "justify": "Subtitle  Alignment",
                "subtitle": "Hard Subtitle Styles",
                "trans": "Subtitle Translation",
                "dubbing": "Dubbing Adjustments"
            }

            self.titles = {
                "homedir": "Set Home directory",
                "ai302_models": "302.ai Translation Models",
                "ai302tts_models": "302.ai TTS Models",
                "openairecognapi_model": "OpenAI Speech",
                "lang": "Software Interface Language",
                "crf": "Video Transcoding Loss Control",
                "cuda_qp": "NVIDIA Use QP Instead of CRF",
                "preset": "Output Video Quality",
                "ffmpeg_cmd": "Custom FFmpeg Command Parameters",
                "video_codec": "H.264 or H.265 Video Encoding",
                "chatgpt_model": "ChatGPT Model List",
                "openaitts_model": "OpenAI TTS models",
                "azure_model": "Azure Model List",
                "localllm_model": "Local LLM Model List",
                "zijiehuoshan_model": "Byte Volcano Inference Access Point",
                "model_list": "Models for Faster and OpenAI",
                "audio_rate": "Maximum Audio Speed Multiplier",
                "video_rate": "Video Slow Motion Multiplier",
                "remove_silence": "Remove End Silence in Dubbing",
                "remove_srt_silence": "Remove Silence Exceeding Dubbing Duration",
                "remove_white_ms": "Remove Silence Between Subtitles",
                "force_edit_srt": "Force Edit Subtitle Timing",
                "bgm_split_time": "bgm segment time/s",
                "vad": "Enable VAD",
                "overall_silence": "Minimum Silence Segment",
                "overall_maxsecs": "Maximum Speech Duration",
                "overall_threshold": "VAD Threshold",
                "overall_speech_pad_ms": "VAD Speech Padding",
                "voice_silence": "Silence Segment in Equal Division",
                "interval_split": "Segment Duration in Equal Division",
                "trans_thread": "Number of Subtitles Translated Simultaneously",
                "retries": "Number of Retries on Translation Failure",
                "dubbing_thread": "Number of Subtitles Dubbed Simultaneously",
                "countdown_sec": "Countdown Seconds on Pause",
                "backaudio_volume": "Background Volume Multiplier",
                "loop_backaudio": "Loop Background Audio",
                "cuda_com_type": "CUDA Data Type",
                "initial_prompt_zh": "Whisper Model Prompt",
                "whisper_threads": "Faster-Whisper CPU Threads",
                "whisper_worker": "Faster-Whisper Working Threads",
                "beam_size": "Subtitle Recognition Accuracy Control 1",
                "best_of": "Subtitle Recognition Accuracy Control 2",
                "temperature": "Faster-Whisper Temperature Control",
                "condition_on_previous_text": "Context Awareness",
                "fontsize": "Hard Subtitle Font Size",
                "fontname": "Hard Subtitle Font Name",
                "fontcolor": "Font Color",
                "fontbordercolor": "Font Border Color",
                "subtitle_bottom": "Subtitle Vertical Offset",
                "cjk_len": "CJK Hard Subtitle Line Length",
                "other_len": "Other Language Hard Subtitle Line Length",
                "zh_hant_s": "Traditional to Simplified Chinese Conversion",
                "azure_lines": "Azure TTS Batch Line Count",
                "chattts_voice": "ChatTTS Voice Tone Value",
                "translation_wait": "Pause Time After Translation",
                "gemini_model": "Gemini Model List"
            }
        self.alertnotice = {}
        # 界面语言
        # tmp = QtWidgets.QHBoxLayout()
        label_title = QtWidgets.QLabel()
        label_title.setText(
            "点击左侧标题将弹出帮助说明" if config.defaulelang == 'zh' else 'Clicking  title on the left will show help ')
        label_title.setObjectName(f"label_head")
        label_title.setAlignment(Qt.AlignCenter)
        label_title.setStyleSheet("""color:#eeeeee;text-align:center""")
        # tmp.addWidget(label_title)
        box.layout().addWidget(label_title)
        helptext = 'show help' if config.defaulelang != 'zh' else '点击查看帮助信息'
        for headkey, item in self.notices.items():
            label_title = QtWidgets.QLabel()
            label_title.setText("↓" + self.heads[headkey])
            label_title.setStyleSheet("""color:#999999""")
            label_title.setObjectName(f"label_{headkey}")
            box.layout().addWidget(label_title)
            for key, val in item.items():
                self.alertnotice[key] = val
                tmp = QtWidgets.QHBoxLayout()
                tmp_0 = QtWidgets.QPushButton()
                tmp_0.setStyleSheet("""background-color:transparent;text-align:right""")
                tmp_0.setFixedWidth(250)
                tmp_0.setText(self.titles[key])
                tmp_0.setObjectName(f'btn_{key}')
                tmp_0.setToolTip(helptext)
                tmp_0.setCursor(Qt.PointingHandCursor)
                if key == 'homedir':
                    tmp_1 = QtWidgets.QPushButton()
                    tmp_1.setCursor(Qt.PointingHandCursor)
                    tmp_1.setText(str(config.settings[key]) if key in config.settings else "")
                    tmp_1.setToolTip(
                        '点击设置家目录，用于保存视频分离、字幕翻译、字幕配音等结果文件' if config.defaulelang == 'zh' else 'Click on Set Home Directory to save the result files for video separation, subtitle translation, subtitle dubbing, etc.')
                    tmp_1.clicked.connect(lambda: self.get_target(tmp_1))
                else:
                    tmp_1 = QtWidgets.QLineEdit()
                    tmp_1.setMinimumSize(QtCore.QSize(0, 30))
                    tmp_1.setText(str(config.settings[key]) if key in config.settings else "")
                    tmp_1.setToolTip(val)
                    tmp_1.setPlaceholderText(val)
                    tmp_1.setObjectName(key)
                    if key == 'ai302tts_models':
                        tmp_1.setReadOnly(True)

                tmp.addWidget(tmp_0)
                tmp.addWidget(tmp_1)
                box.layout().addLayout(tmp)

        box.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_area.setWidget(box)
        self.layout.addWidget(scroll_area)

        self.set_ok = QtWidgets.QPushButton(setini)
        self.set_ok.setGeometry(QtCore.QRect(325, 620, 150, 35))
        self.set_ok.setMinimumSize(QtCore.QSize(0, 35))
        self.set_ok.setObjectName("set_ok")

        self.retranslateUi(setini)
        QtCore.QMetaObject.connectSlotsByName(setini)

    def retranslateUi(self, setini):
        setini.setWindowTitle('选项' if config.defaulelang == 'zh' else 'Options')
        self.set_ok.setText('保存并关闭' if config.defaulelang == 'zh' else "Save and Close")
