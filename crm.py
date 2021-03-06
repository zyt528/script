# coding=utf-8

# import mysql.connector
import pymysql

def get_all_zj_users():
    user_list = list()
    success_list = list()
    response_json = {
    "tag": "d3ae7802-28a5-44f4-9044-2eaf3c88d53e",
    "type": 1,
    "interface": "user.select",
    "success": [
        {
            "name": "常熟分公司",
            "is_hide": 0,
            "gid": 2048,
            "father_id": 2199,
            "users": []
        },
        {
            "name": "绵阳分公司",
            "is_hide": 0,
            "gid": 2049,
            "father_id": 2202,
            "users": []
        },
        {
            "name": "咸阳分公司",
            "is_hide": 0,
            "gid": 2050,
            "father_id": 2198,
            "users": []
        },
        {
            "name": "人力资源与行政中心",
            "is_hide": 0,
            "gid": 3,
            "father_id": 0,
            "users": [
                {
                    "uid": 14089,
                    "username": "t1"
                },
                {
                    "uid": 14090,
                    "username": "t2"
                },
                {
                    "uid": 15022,
                    "username": "panco.yu"
                },
                {
                    "uid": 15396,
                    "username": "admin"
                }
            ]
        },
        {
            "name": "太原分公司",
            "is_hide": 0,
            "gid": 2051,
            "father_id": 2197,
            "users": []
        },
        {
            "name": "B端产品部",
            "is_hide": 1,
            "gid": 2052,
            "father_id": 1655,
            "users": []
        },
        {
            "name": "家装运营部",
            "is_hide": 0,
            "gid": 6,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "标准化分公司BP组",
            "is_hide": 0,
            "gid": 2054,
            "father_id": 1129,
            "users": [
                {
                    "uid": 16368,
                    "username": "jack.sui"
                }
            ]
        },
        {
            "name": "技术与产业效率中心",
            "is_hide": 1,
            "gid": 7,
            "father_id": 0,
            "users": []
        },
        {
            "name": "平台五区",
            "is_hide": 1,
            "gid": 2055,
            "father_id": 1942,
            "users": []
        },
        {
            "name": "宁波BP",
            "is_hide": 0,
            "gid": 2056,
            "father_id": 1945,
            "users": []
        },
        {
            "name": "徐州BP",
            "is_hide": 0,
            "gid": 2057,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "扬州BP",
            "is_hide": 0,
            "gid": 2058,
            "father_id": 1944,
            "users": []
        },
        {
            "name": "常熟BP",
            "is_hide": 0,
            "gid": 2059,
            "father_id": 1944,
            "users": []
        },
        {
            "name": "南通BP",
            "is_hide": 0,
            "gid": 2060,
            "father_id": 1944,
            "users": []
        },
        {
            "name": "嘉兴BP",
            "is_hide": 0,
            "gid": 2061,
            "father_id": 1945,
            "users": []
        },
        {
            "name": "惠州BP",
            "is_hide": 0,
            "gid": 2062,
            "father_id": 2174,
            "users": []
        },
        {
            "name": "中山BP",
            "is_hide": 0,
            "gid": 2063,
            "father_id": 2174,
            "users": []
        },
        {
            "name": "青岛BP",
            "is_hide": 0,
            "gid": 2064,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "济南BP",
            "is_hide": 0,
            "gid": 2065,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "绵阳BP",
            "is_hide": 0,
            "gid": 2066,
            "father_id": 1947,
            "users": []
        },
        {
            "name": "太原BP",
            "is_hide": 0,
            "gid": 2067,
            "father_id": 1946,
            "users": []
        },
        {
            "name": "咸阳BP",
            "is_hide": 0,
            "gid": 2068,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "廊坊BP",
            "is_hide": 0,
            "gid": 2069,
            "father_id": 1946,
            "users": []
        },
        {
            "name": "哈尔滨BP",
            "is_hide": 0,
            "gid": 2070,
            "father_id": 1946,
            "users": []
        },
        {
            "name": "衡阳BP",
            "is_hide": 0,
            "gid": 2071,
            "father_id": 1947,
            "users": []
        },
        {
            "name": "石家庄BP",
            "is_hide": 0,
            "gid": 2072,
            "father_id": 1946,
            "users": []
        },
        {
            "name": "长春BP",
            "is_hide": 0,
            "gid": 2073,
            "father_id": 1946,
            "users": []
        },
        {
            "name": "财务中心",
            "is_hide": 0,
            "gid": 26,
            "father_id": 0,
            "users": [
                {
                    "uid": 738861,
                    "username": "jacky.liu"
                },
                {
                    "uid": 728370,
                    "username": "andre.li"
                }
            ]
        },
        {
            "name": "珠海BP",
            "is_hide": 0,
            "gid": 2074,
            "father_id": 2174,
            "users": []
        },
        {
            "name": "赣州BP",
            "is_hide": 0,
            "gid": 2075,
            "father_id": 2174,
            "users": []
        },
        {
            "name": "宁波运营组",
            "is_hide": 0,
            "gid": 2076,
            "father_id": 2030,
            "users": [
                {
                    "uid": 74348,
                    "username": "alvinm.ma"
                },
                {
                    "uid": 10035,
                    "username": "edward.li"
                },
                {
                    "uid": 92513,
                    "username": "kninght.li"
                }
            ]
        },
        {
            "name": "宁波市",
            "is_hide": 0,
            "gid": 2077,
            "father_id": 2322,
            "users": [
                {
                    "uid": 82945,
                    "username": "pengjin.huang"
                },
                {
                    "uid": 14499,
                    "username": "taylor.wu"
                }
            ]
        },
        {
            "name": "嘉兴运营组",
            "is_hide": 0,
            "gid": 2078,
            "father_id": 2046,
            "users": []
        },
        {
            "name": "嘉兴市",
            "is_hide": 0,
            "gid": 2079,
            "father_id": 2325,
            "users": [
                {
                    "uid": 10410,
                    "username": "zhirong.zhang"
                }
            ]
        },
        {
            "name": "青岛运营组",
            "is_hide": 0,
            "gid": 2080,
            "father_id": 2026,
            "users": [
                {
                    "uid": 740346,
                    "username": "teague.lu"
                },
                {
                    "uid": 733688,
                    "username": "win.zhang"
                },
                {
                    "uid": 30233,
                    "username": "lifang.hu"
                }
            ]
        },
        {
            "name": "青岛市",
            "is_hide": 0,
            "gid": 2081,
            "father_id": 1840,
            "users": [
                {
                    "uid": 89741,
                    "username": "mason.wang"
                },
                {
                    "uid": 10097,
                    "username": "quinton.zhang"
                },
                {
                    "uid": 12347,
                    "username": "hardy.li"
                },
                {
                    "uid": 12585,
                    "username": "vincent.wang"
                }
            ]
        },
        {
            "name": "济南运营组",
            "is_hide": 0,
            "gid": 2082,
            "father_id": 2040,
            "users": [
                {
                    "uid": 739960,
                    "username": "jill.wang"
                }
            ]
        },
        {
            "name": "济南市",
            "is_hide": 0,
            "gid": 2083,
            "father_id": 1840,
            "users": [
                {
                    "uid": 12453,
                    "username": "violin.wang"
                },
                {
                    "uid": 12454,
                    "username": "arno.shi"
                }
            ]
        },
        {
            "name": "珠海运营组",
            "is_hide": 0,
            "gid": 2084,
            "father_id": 2029,
            "users": [
                {
                    "uid": 1574,
                    "username": "cash.wu"
                },
                {
                    "uid": 741811,
                    "username": "eason.ye"
                },
                {
                    "uid": 747172,
                    "username": "jrock.wu"
                }
            ]
        },
        {
            "name": "珠海市",
            "is_hide": 0,
            "gid": 2085,
            "father_id": 1834,
            "users": [
                {
                    "uid": 17756,
                    "username": "joe.feng"
                },
                {
                    "uid": 14275,
                    "username": "chris.meng"
                }
            ]
        },
        {
            "name": "运营平台组",
            "is_hide": 0,
            "gid": 38,
            "father_id": 192768,
            "users": [
                {
                    "uid": 1067,
                    "username": "jacky.yao"
                },
                {
                    "uid": 14970,
                    "username": "lotus.kong"
                },
                {
                    "uid": 15718,
                    "username": "airrie.mao"
                }
            ]
        },
        {
            "name": "惠州运营组",
            "is_hide": 0,
            "gid": 2086,
            "father_id": 2028,
            "users": [
                {
                    "uid": 745303,
                    "username": "julius.xu"
                },
                {
                    "uid": 10173,
                    "username": "will.zhang"
                },
                {
                    "uid": 10414,
                    "username": "winter.fan"
                }
            ]
        },
        {
            "name": "惠州市",
            "is_hide": 0,
            "gid": 2087,
            "father_id": 2331,
            "users": [
                {
                    "uid": 1509,
                    "username": "mark.huang"
                },
                {
                    "uid": 11428,
                    "username": "seedling.zhou"
                },
                {
                    "uid": 12486,
                    "username": "sinchy.li"
                }
            ]
        },
        {
            "name": "中山运营组",
            "is_hide": 0,
            "gid": 2088,
            "father_id": 2045,
            "users": [
                {
                    "uid": 10011,
                    "username": "timson.yang"
                }
            ]
        },
        {
            "name": "中山市",
            "is_hide": 0,
            "gid": 2089,
            "father_id": 2332,
            "users": [
                {
                    "uid": 1436,
                    "username": "gentle.zheng"
                },
                {
                    "uid": 10714,
                    "username": "warren.chen"
                }
            ]
        },
        {
            "name": "徐州运营组",
            "is_hide": 0,
            "gid": 2090,
            "father_id": 2031,
            "users": [
                {
                    "uid": 747493,
                    "username": "tonghe.liu"
                }
            ]
        },
        {
            "name": "徐州市",
            "is_hide": 0,
            "gid": 2091,
            "father_id": 1840,
            "users": [
                {
                    "uid": 92225,
                    "username": "arthur.fan"
                },
                {
                    "uid": 14244,
                    "username": "jason.gong"
                }
            ]
        },
        {
            "name": "扬州运营组",
            "is_hide": 0,
            "gid": 2092,
            "father_id": 2032,
            "users": [
                {
                    "uid": 10631,
                    "username": "jack.lu"
                },
                {
                    "uid": 14242,
                    "username": "jane.yue"
                }
            ]
        },
        {
            "name": "运维与企业IT部",
            "is_hide": 0,
            "gid": 45,
            "father_id": 583,
            "users": [
                {
                    "uid": 1002,
                    "username": "tuorizwb"
                },
                {
                    "uid": 12623,
                    "username": "loong.zhou"
                }
            ]
        },
        {
            "name": "扬州市",
            "is_hide": 0,
            "gid": 2093,
            "father_id": 1836,
            "users": [
                {
                    "uid": 17089,
                    "username": "jian.xu"
                },
                {
                    "uid": 17664,
                    "username": "bingjie.chen"
                },
                {
                    "uid": 10630,
                    "username": "jimmy.yan"
                }
            ]
        },
        {
            "name": "南通运营组",
            "is_hide": 0,
            "gid": 2094,
            "father_id": 2047,
            "users": [
                {
                    "uid": 10020,
                    "username": "jason.tang"
                },
                {
                    "uid": 736007,
                    "username": "lee.xu"
                }
            ]
        },
        {
            "name": "南通市",
            "is_hide": 0,
            "gid": 2095,
            "father_id": 2330,
            "users": [
                {
                    "uid": 10665,
                    "username": "sea.wang"
                }
            ]
        },
        {
            "name": "常熟运营组",
            "is_hide": 0,
            "gid": 2096,
            "father_id": 2048,
            "users": [
                {
                    "uid": 30147,
                    "username": "dick.xu"
                }
            ]
        },
        {
            "name": "常熟市",
            "is_hide": 0,
            "gid": 2097,
            "father_id": 2330,
            "users": [
                {
                    "uid": 11045,
                    "username": "nicolas.wu"
                }
            ]
        },
        {
            "name": "绵阳运营组",
            "is_hide": 0,
            "gid": 2098,
            "father_id": 2049,
            "users": [
                {
                    "uid": 738039,
                    "username": "jenyd.jing"
                }
            ]
        },
        {
            "name": "绵阳市",
            "is_hide": 0,
            "gid": 2099,
            "father_id": 2335,
            "users": [
                {
                    "uid": 16165,
                    "username": "abner.xu"
                }
            ]
        },
        {
            "name": "咸阳运营组",
            "is_hide": 0,
            "gid": 2100,
            "father_id": 2050,
            "users": [
                {
                    "uid": 30146,
                    "username": "bear.guo"
                }
            ]
        },
        {
            "name": "咸阳市",
            "is_hide": 0,
            "gid": 2101,
            "father_id": 2336,
            "users": []
        },
        {
            "name": "太原运营组",
            "is_hide": 0,
            "gid": 2102,
            "father_id": 2051,
            "users": [
                {
                    "uid": 745587,
                    "username": "eric.lin"
                },
                {
                    "uid": 735110,
                    "username": "jie.gao"
                },
                {
                    "uid": 15455,
                    "username": "fone.pan"
                }
            ]
        },
        {
            "name": "太原市",
            "is_hide": 0,
            "gid": 2103,
            "father_id": 2327,
            "users": [
                {
                    "uid": 11011,
                    "username": "kobe.li"
                },
                {
                    "uid": 14130,
                    "username": "brook.zhang"
                }
            ]
        },
        {
            "name": "赣州运营组",
            "is_hide": 0,
            "gid": 2104,
            "father_id": 2033,
            "users": []
        },
        {
            "name": "赣州市",
            "is_hide": 0,
            "gid": 2105,
            "father_id": 2331,
            "users": [
                {
                    "uid": 11290,
                    "username": "kent.cai"
                }
            ]
        },
        {
            "name": "廊坊运营组",
            "is_hide": 0,
            "gid": 2106,
            "father_id": 2027,
            "users": [
                {
                    "uid": 1556,
                    "username": "roy.zhang"
                }
            ]
        },
        {
            "name": "廊坊市",
            "is_hide": 0,
            "gid": 2107,
            "father_id": 1837,
            "users": [
                {
                    "uid": 89460,
                    "username": "lwan.yi"
                },
                {
                    "uid": 89496,
                    "username": "bing.zhang"
                },
                {
                    "uid": 11016,
                    "username": "sanyu.song"
                },
                {
                    "uid": 12508,
                    "username": "baldwin.liu"
                }
            ]
        },
        {
            "name": "衡阳运营组",
            "is_hide": 0,
            "gid": 2108,
            "father_id": 2041,
            "users": []
        },
        {
            "name": "衡阳市",
            "is_hide": 0,
            "gid": 2109,
            "father_id": 2334,
            "users": [
                {
                    "uid": 10715,
                    "username": "houston.hou"
                }
            ]
        },
        {
            "name": "石家庄运营组",
            "is_hide": 0,
            "gid": 2110,
            "father_id": 2042,
            "users": [
                {
                    "uid": 745543,
                    "username": "will.wang"
                }
            ]
        },
        {
            "name": "石家庄市",
            "is_hide": 0,
            "gid": 2111,
            "father_id": 2327,
            "users": [
                {
                    "uid": 12405,
                    "username": "leovy.dai"
                },
                {
                    "uid": 12408,
                    "username": "bob.chang"
                }
            ]
        },
        {
            "name": "哈尔滨运营组",
            "is_hide": 0,
            "gid": 2112,
            "father_id": 2043,
            "users": [
                {
                    "uid": 11126,
                    "username": "dick.lu"
                },
                {
                    "uid": 96588,
                    "username": "alex.meng"
                },
                {
                    "uid": 736797,
                    "username": "lin.yu"
                },
                {
                    "uid": 736796,
                    "username": "zhen.yang"
                }
            ]
        },
        {
            "name": "哈尔滨市",
            "is_hide": 0,
            "gid": 2113,
            "father_id": 2326,
            "users": [
                {
                    "uid": 11208,
                    "username": "sam.li"
                }
            ]
        },
        {
            "name": "长春运营组",
            "is_hide": 0,
            "gid": 2114,
            "father_id": 2044,
            "users": [
                {
                    "uid": 1648,
                    "username": "ivy.zhao"
                },
                {
                    "uid": 740868,
                    "username": "rabbit.song"
                },
                {
                    "uid": 741149,
                    "username": "moon.zhao"
                },
                {
                    "uid": 747002,
                    "username": "zhida.li"
                }
            ]
        },
        {
            "name": "市场营销中心",
            "is_hide": 0,
            "gid": 67,
            "father_id": 0,
            "users": [
                {
                    "uid": 738215,
                    "username": "ellar.yang"
                }
            ]
        },
        {
            "name": "长春市",
            "is_hide": 0,
            "gid": 2115,
            "father_id": 2326,
            "users": [
                {
                    "uid": 14212,
                    "username": "jack.guo"
                }
            ]
        },
        {
            "name": "大客户部",
            "is_hide": 1,
            "gid": 2116,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "助理部",
            "is_hide": 1,
            "gid": 69,
            "father_id": 1615,
            "users": []
        },
        {
            "name": "运营部",
            "is_hide": 1,
            "gid": 2117,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "市场部",
            "is_hide": 0,
            "gid": 2118,
            "father_id": 195824,
            "users": [
                {
                    "uid": 1444,
                    "username": "rick.huang"
                }
            ]
        },
        {
            "name": "支持部",
            "is_hide": 1,
            "gid": 2119,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "泉州市",
            "is_hide": 0,
            "gid": 2120,
            "father_id": 2324,
            "users": [
                {
                    "uid": 14718,
                    "username": "dargon.chen"
                }
            ]
        },
        {
            "name": "温州市",
            "is_hide": 0,
            "gid": 2121,
            "father_id": 2322,
            "users": [
                {
                    "uid": 12541,
                    "username": "lven.yue"
                }
            ]
        },
        {
            "name": "镇江市",
            "is_hide": 0,
            "gid": 2122,
            "father_id": 2328,
            "users": [
                {
                    "uid": 12472,
                    "username": "yves.wang"
                }
            ]
        },
        {
            "name": "清远监理组",
            "is_hide": 1,
            "gid": 2123,
            "father_id": 1834,
            "users": []
        },
        {
            "name": "南充市",
            "is_hide": 0,
            "gid": 2124,
            "father_id": 2335,
            "users": [
                {
                    "uid": 12613,
                    "username": "max.liu"
                }
            ]
        },
        {
            "name": "清远分公司",
            "is_hide": 0,
            "gid": 2125,
            "father_id": 2201,
            "users": []
        },
        {
            "name": "清远运营组",
            "is_hide": 0,
            "gid": 2126,
            "father_id": 2125,
            "users": [
                {
                    "uid": 741151,
                    "username": "lethe.chen"
                }
            ]
        },
        {
            "name": "泉州分公司",
            "is_hide": 0,
            "gid": 2127,
            "father_id": 2200,
            "users": []
        },
        {
            "name": "泉州运营组",
            "is_hide": 0,
            "gid": 2128,
            "father_id": 2127,
            "users": [
                {
                    "uid": 738750,
                    "username": "van.xie"
                },
                {
                    "uid": 738757,
                    "username": "silence.yang"
                }
            ]
        },
        {
            "name": "温州分公司",
            "is_hide": 0,
            "gid": 2129,
            "father_id": 2200,
            "users": []
        },
        {
            "name": "温州运营组",
            "is_hide": 0,
            "gid": 2130,
            "father_id": 2129,
            "users": [
                {
                    "uid": 18090,
                    "username": "jiaqi.li"
                },
                {
                    "uid": 746773,
                    "username": "yao.chen"
                }
            ]
        },
        {
            "name": "镇江分公司",
            "is_hide": 0,
            "gid": 2131,
            "father_id": 2199,
            "users": []
        },
        {
            "name": "镇江运营组",
            "is_hide": 0,
            "gid": 2132,
            "father_id": 2131,
            "users": [
                {
                    "uid": 96589,
                    "username": "nico.hu"
                },
                {
                    "uid": 735663,
                    "username": "acton.chen"
                }
            ]
        },
        {
            "name": "南充分公司",
            "is_hide": 0,
            "gid": 2133,
            "father_id": 2202,
            "users": []
        },
        {
            "name": "南充运营组",
            "is_hide": 0,
            "gid": 2134,
            "father_id": 2133,
            "users": []
        },
        {
            "name": "用户口碑中心",
            "is_hide": 1,
            "gid": 2135,
            "father_id": 0,
            "users": []
        },
        {
            "name": "镇江BP",
            "is_hide": 0,
            "gid": 2136,
            "father_id": 1944,
            "users": []
        },
        {
            "name": "温州BP",
            "is_hide": 0,
            "gid": 2137,
            "father_id": 1945,
            "users": []
        },
        {
            "name": "泉州BP",
            "is_hide": 0,
            "gid": 2138,
            "father_id": 1945,
            "users": []
        },
        {
            "name": "南充BP",
            "is_hide": 0,
            "gid": 2139,
            "father_id": 1947,
            "users": []
        },
        {
            "name": "清远BP",
            "is_hide": 0,
            "gid": 2140,
            "father_id": 2174,
            "users": []
        },
        {
            "name": "大数据部",
            "is_hide": 0,
            "gid": 2141,
            "father_id": 1366,
            "users": [
                {
                    "uid": 2056,
                    "username": "data_test"
                },
                {
                    "uid": 56629,
                    "username": "winston.wu"
                }
            ]
        },
        {
            "name": "回访服务部",
            "is_hide": 0,
            "gid": 2142,
            "father_id": 2231,
            "users": [
                {
                    "uid": 1251,
                    "username": "nina.wei"
                }
            ]
        },
        {
            "name": "落地回访一组",
            "is_hide": 1,
            "gid": 2143,
            "father_id": 2142,
            "users": []
        },
        {
            "name": "落地回访二组",
            "is_hide": 1,
            "gid": 2144,
            "father_id": 2142,
            "users": []
        },
        {
            "name": "总裁办",
            "is_hide": 0,
            "gid": 97,
            "father_id": 0,
            "users": [
                {
                    "uid": 1331,
                    "username": "robin"
                },
                {
                    "uid": 1708,
                    "username": "light.huang"
                }
            ]
        },
        {
            "name": "非落地回访组",
            "is_hide": 0,
            "gid": 2145,
            "father_id": 2142,
            "users": [
                {
                    "uid": 17456,
                    "username": "beck.deng"
                },
                {
                    "uid": 17972,
                    "username": "wanji.li"
                },
                {
                    "uid": 18107,
                    "username": "deyu.kong"
                },
                {
                    "uid": 746121,
                    "username": "lun.liao"
                },
                {
                    "uid": 11585,
                    "username": "mi.su"
                },
                {
                    "uid": 11725,
                    "username": "owen.wen"
                },
                {
                    "uid": 15017,
                    "username": "clearlove.qu"
                }
            ]
        },
        {
            "name": "北三组",
            "is_hide": 0,
            "gid": 2146,
            "father_id": 2261,
            "users": [
                {
                    "uid": 17441,
                    "username": "amelia.wu"
                },
                {
                    "uid": 18023,
                    "username": "derrick.wei"
                },
                {
                    "uid": 1776,
                    "username": "memory.zhang"
                },
                {
                    "uid": 740059,
                    "username": "niseko.xie"
                },
                {
                    "uid": 742518,
                    "username": "gf.wang"
                },
                {
                    "uid": 10197,
                    "username": "ann.zhong"
                },
                {
                    "uid": 14796,
                    "username": "lyon.he"
                },
                {
                    "uid": 15575,
                    "username": "jeffery.wu"
                },
                {
                    "uid": 16129,
                    "username": "grace.chen"
                },
                {
                    "uid": 737183,
                    "username": "chanyeol.zeng"
                },
                {
                    "uid": 737187,
                    "username": "shenqiang.yang"
                },
                {
                    "uid": 737186,
                    "username": "betty.liang"
                }
            ]
        },
        {
            "name": "核算二部",
            "is_hide": 0,
            "gid": 2147,
            "father_id": 26,
            "users": [
                {
                    "uid": 30138,
                    "username": "lisa.fan"
                }
            ]
        },
        {
            "name": "南山店",
            "is_hide": 0,
            "gid": 2148,
            "father_id": 1582,
            "users": [
                {
                    "uid": 10494,
                    "username": "amy.peng"
                }
            ]
        },
        {
            "name": "龙岗店",
            "is_hide": 0,
            "gid": 2149,
            "father_id": 1582,
            "users": []
        },
        {
            "name": "广州BP",
            "is_hide": 0,
            "gid": 102,
            "father_id": 2054,
            "users": []
        },
        {
            "name": "南山设计一部",
            "is_hide": 0,
            "gid": 2150,
            "father_id": 2148,
            "users": [
                {
                    "uid": 17159,
                    "username": "hairley.wang"
                },
                {
                    "uid": 17641,
                    "username": "gailun.yang"
                },
                {
                    "uid": 11325,
                    "username": "alice.ye"
                },
                {
                    "uid": 11343,
                    "username": "jason.liu"
                },
                {
                    "uid": 14191,
                    "username": "moses.liu"
                },
                {
                    "uid": 15403,
                    "username": "lulu.deng"
                }
            ]
        },
        {
            "name": "南山设计二部",
            "is_hide": 0,
            "gid": 2151,
            "father_id": 2148,
            "users": [
                {
                    "uid": 17414,
                    "username": "alex.ouyang"
                },
                {
                    "uid": 17605,
                    "username": "seven.dong"
                },
                {
                    "uid": 30227,
                    "username": "daisy.zhang"
                },
                {
                    "uid": 16335,
                    "username": "nick.tang"
                }
            ]
        },
        {
            "name": "南山设计三部",
            "is_hide": 0,
            "gid": 2152,
            "father_id": 2148,
            "users": [
                {
                    "uid": 76017,
                    "username": "dick.ye"
                },
                {
                    "uid": 15229,
                    "username": "cici.zhou"
                }
            ]
        },
        {
            "name": "南山设计四部",
            "is_hide": 0,
            "gid": 2153,
            "father_id": 2148,
            "users": [
                {
                    "uid": 11562,
                    "username": "chris.ouyang"
                },
                {
                    "uid": 11703,
                    "username": "adolph.jun"
                },
                {
                    "uid": 12528,
                    "username": "white.yin"
                },
                {
                    "uid": 15456,
                    "username": "buhuozhuanyuan"
                },
                {
                    "uid": 15821,
                    "username": "xianghe.zhao"
                },
                {
                    "uid": 15915,
                    "username": "hard.chen"
                },
                {
                    "uid": 16080,
                    "username": "hero.xiong"
                }
            ]
        },
        {
            "name": "南山市场部",
            "is_hide": 0,
            "gid": 2154,
            "father_id": 2148,
            "users": [
                {
                    "uid": 16660,
                    "username": "anor.huang"
                },
                {
                    "uid": 17165,
                    "username": "judy.luo"
                },
                {
                    "uid": 1502,
                    "username": "mia.chen"
                },
                {
                    "uid": 15961,
                    "username": "kristy.pan"
                }
            ]
        },
        {
            "name": "龙岗设计一部",
            "is_hide": 0,
            "gid": 2155,
            "father_id": 2149,
            "users": [
                {
                    "uid": 17466,
                    "username": "ellen.lao"
                },
                {
                    "uid": 76019,
                    "username": "zom.li"
                },
                {
                    "uid": 11313,
                    "username": "daniel.chen"
                },
                {
                    "uid": 11399,
                    "username": "sandy.liu"
                },
                {
                    "uid": 30243,
                    "username": "xiao.zhong"
                },
                {
                    "uid": 80397,
                    "username": "fly.teng"
                },
                {
                    "uid": 15118,
                    "username": "randy.chen"
                },
                {
                    "uid": 15238,
                    "username": "abigale.wang"
                },
                {
                    "uid": 15337,
                    "username": "kerwin.hong"
                },
                {
                    "uid": 15626,
                    "username": "smilebaby.wu"
                }
            ]
        },
        {
            "name": "龙岗设计二部",
            "is_hide": 0,
            "gid": 2156,
            "father_id": 2149,
            "users": [
                {
                    "uid": 67659,
                    "username": "cici.long"
                },
                {
                    "uid": 56566,
                    "username": "menben.li"
                },
                {
                    "uid": 56606,
                    "username": "emma.yu"
                },
                {
                    "uid": 30230,
                    "username": "sky.yue"
                },
                {
                    "uid": 14125,
                    "username": "willie.li"
                },
                {
                    "uid": 15233,
                    "username": "jarvan.hu"
                }
            ]
        },
        {
            "name": "行政部",
            "is_hide": 0,
            "gid": 109,
            "father_id": 3,
            "users": [
                {
                    "uid": 17408,
                    "username": "cwzx"
                },
                {
                    "uid": 84776,
                    "username": "lucae.li"
                },
                {
                    "uid": 12681,
                    "username": "linda.chen"
                },
                {
                    "uid": 13848,
                    "username": "gloria.chen"
                },
                {
                    "uid": 13933,
                    "username": "ann.tang"
                },
                {
                    "uid": 14093,
                    "username": "t3"
                },
                {
                    "uid": 14094,
                    "username": "t4"
                },
                {
                    "uid": 16143,
                    "username": "alicia.lin"
                }
            ]
        },
        {
            "name": "龙岗设计三部",
            "is_hide": 0,
            "gid": 2157,
            "father_id": 2149,
            "users": [
                {
                    "uid": 17350,
                    "username": "jacky.zhu"
                },
                {
                    "uid": 85800,
                    "username": "stephan.yao"
                },
                {
                    "uid": 56605,
                    "username": "july.su"
                },
                {
                    "uid": 56680,
                    "username": "danae.huang"
                },
                {
                    "uid": 30136,
                    "username": "alittle.zhu"
                },
                {
                    "uid": 30168,
                    "username": "ricky.yuan"
                },
                {
                    "uid": 30172,
                    "username": "ruoyu.lin"
                },
                {
                    "uid": 14571,
                    "username": "rivers.jiang"
                },
                {
                    "uid": 15602,
                    "username": "alan.peng"
                }
            ]
        },
        {
            "name": "龙岗市场部",
            "is_hide": 0,
            "gid": 2158,
            "father_id": 2149,
            "users": [
                {
                    "uid": 17216,
                    "username": "sunny.he"
                },
                {
                    "uid": 17322,
                    "username": "fendy.xu"
                },
                {
                    "uid": 10799,
                    "username": "jason.jiao"
                },
                {
                    "uid": 76631,
                    "username": "dream.li"
                },
                {
                    "uid": 77630,
                    "username": "sunshiney.zhou"
                },
                {
                    "uid": 30289,
                    "username": "plum.li"
                },
                {
                    "uid": 16145,
                    "username": "rain.wu"
                },
                {
                    "uid": 16268,
                    "username": "potato.yu"
                }
            ]
        },
        {
            "name": "交付东区",
            "is_hide": 0,
            "gid": 2159,
            "father_id": 1926,
            "users": [
                {
                    "uid": 16616,
                    "username": "edward.qiu"
                },
                {
                    "uid": 10412,
                    "username": "kang.kang"
                },
                {
                    "uid": 10617,
                    "username": "jason.zhou"
                },
                {
                    "uid": 30209,
                    "username": "jiehao.ni"
                },
                {
                    "uid": 16039,
                    "username": "soar.liu"
                }
            ]
        },
        {
            "name": "交付西区",
            "is_hide": 0,
            "gid": 2160,
            "father_id": 1926,
            "users": [
                {
                    "uid": 18415,
                    "username": "franz.zhang"
                },
                {
                    "uid": 10716,
                    "username": "john.liu"
                },
                {
                    "uid": 11370,
                    "username": "zemel.zheng"
                },
                {
                    "uid": 14265,
                    "username": "geoff.chen"
                },
                {
                    "uid": 14276,
                    "username": "beck.yu"
                },
                {
                    "uid": 14361,
                    "username": "loren.luo"
                }
            ]
        },
        {
            "name": "体系组",
            "is_hide": 1,
            "gid": 2161,
            "father_id": 97,
            "users": []
        },
        {
            "name": "移动研发部",
            "is_hide": 0,
            "gid": 2167,
            "father_id": 583,
            "users": []
        },
        {
            "name": "前端研发部",
            "is_hide": 0,
            "gid": 2168,
            "father_id": 583,
            "users": [
                {
                    "uid": 12868,
                    "username": "carl.wu"
                }
            ]
        },
        {
            "name": "产业创新研发部",
            "is_hide": 0,
            "gid": 2169,
            "father_id": 583,
            "users": [
                {
                    "uid": 11182,
                    "username": "sampson.qi"
                }
            ]
        },
        {
            "name": "运营部",
            "is_hide": 0,
            "gid": 2170,
            "father_id": 1609,
            "users": [
                {
                    "uid": 82221,
                    "username": "ben.liu"
                },
                {
                    "uid": 65851,
                    "username": "smile.xiao"
                },
                {
                    "uid": 86665,
                    "username": "donfan.liao"
                },
                {
                    "uid": 86664,
                    "username": "jack.tan"
                },
                {
                    "uid": 87459,
                    "username": "lisae.li"
                },
                {
                    "uid": 88510,
                    "username": "jesse.zou"
                },
                {
                    "uid": 88598,
                    "username": "happy.cheng"
                },
                {
                    "uid": 90320,
                    "username": "lydia.wu"
                },
                {
                    "uid": 91496,
                    "username": "amber.liao"
                },
                {
                    "uid": 92748,
                    "username": "nini.ni"
                },
                {
                    "uid": 13712,
                    "username": "carrie.zhu"
                },
                {
                    "uid": 96587,
                    "username": "elsa.shao"
                },
                {
                    "uid": 96609,
                    "username": "lewis.zhou"
                }
            ]
        },
        {
            "name": "中原区域BP组",
            "is_hide": 0,
            "gid": 2173,
            "father_id": 1129,
            "users": [
                {
                    "uid": 1482,
                    "username": "haley.niu"
                }
            ]
        },
        {
            "name": "华南区域BP组",
            "is_hide": 0,
            "gid": 2174,
            "father_id": 1129,
            "users": [
                {
                    "uid": 77,
                    "username": "tuki.zhao"
                }
            ]
        },
        {
            "name": "保定BP",
            "is_hide": 0,
            "gid": 2175,
            "father_id": 1946,
            "users": []
        },
        {
            "name": "洛阳BP",
            "is_hide": 0,
            "gid": 2176,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "潍坊BP",
            "is_hide": 0,
            "gid": 2177,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "烟台BP",
            "is_hide": 0,
            "gid": 2178,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "临沂BP",
            "is_hide": 0,
            "gid": 2179,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "连云港BP",
            "is_hide": 0,
            "gid": 2180,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "宿迁BP",
            "is_hide": 0,
            "gid": 2181,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "淮安BP",
            "is_hide": 0,
            "gid": 2182,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "盐城BP",
            "is_hide": 0,
            "gid": 2183,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "芜湖BP",
            "is_hide": 0,
            "gid": 2184,
            "father_id": 1944,
            "users": []
        },
        {
            "name": "阜阳BP",
            "is_hide": 0,
            "gid": 2185,
            "father_id": 1944,
            "users": []
        },
        {
            "name": "泰州BP",
            "is_hide": 0,
            "gid": 2186,
            "father_id": 1944,
            "users": []
        },
        {
            "name": "遵义BP",
            "is_hide": 0,
            "gid": 2187,
            "father_id": 1947,
            "users": []
        },
        {
            "name": "海口BP",
            "is_hide": 0,
            "gid": 2188,
            "father_id": 2174,
            "users": []
        },
        {
            "name": "襄阳BP",
            "is_hide": 0,
            "gid": 2189,
            "father_id": 1947,
            "users": []
        },
        {
            "name": "宜昌BP",
            "is_hide": 0,
            "gid": 2190,
            "father_id": 1947,
            "users": []
        },
        {
            "name": "业务发展部",
            "is_hide": 0,
            "gid": 2191,
            "father_id": 1609,
            "users": [
                {
                    "uid": 1047,
                    "username": "sunny.liu"
                }
            ]
        },
        {
            "name": "业务运营部",
            "is_hide": 0,
            "gid": 2192,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "渠道部",
            "is_hide": 1,
            "gid": 2193,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "商学院",
            "is_hide": 0,
            "gid": 2194,
            "father_id": 2361,
            "users": [
                {
                    "uid": 16817,
                    "username": "lenna.yang"
                },
                {
                    "uid": 83558,
                    "username": "cc.cao"
                },
                {
                    "uid": 67421,
                    "username": "michelle.zhang"
                },
                {
                    "uid": 83846,
                    "username": "willian.liu"
                },
                {
                    "uid": 739382,
                    "username": "melody.dang"
                },
                {
                    "uid": 747068,
                    "username": "nancy.yao"
                },
                {
                    "uid": 736867,
                    "username": "nancy.ling"
                }
            ]
        },
        {
            "name": "业务支持组",
            "is_hide": 0,
            "gid": 2195,
            "father_id": 2361,
            "users": [
                {
                    "uid": 16517,
                    "username": "circle.yuan"
                },
                {
                    "uid": 1078,
                    "username": "anne.mao"
                },
                {
                    "uid": 1204,
                    "username": "jack.liu"
                },
                {
                    "uid": 731086,
                    "username": "gary.liang"
                },
                {
                    "uid": 11098,
                    "username": "kathy.wang"
                },
                {
                    "uid": 13211,
                    "username": "happy.zhu"
                },
                {
                    "uid": 734709,
                    "username": "anemone.chen"
                },
                {
                    "uid": 14143,
                    "username": "jean.li"
                }
            ]
        },
        {
            "name": "商业分析组",
            "is_hide": 0,
            "gid": 2196,
            "father_id": 2192,
            "users": [
                {
                    "uid": 65856,
                    "username": "laughing.ye"
                },
                {
                    "uid": 90280,
                    "username": "tom.tong"
                },
                {
                    "uid": 77291,
                    "username": "stephanie.huang"
                }
            ]
        },
        {
            "name": "华北区",
            "is_hide": 0,
            "gid": 2197,
            "father_id": 2191,
            "users": [
                {
                    "uid": 83537,
                    "username": "charles.jiang"
                }
            ]
        },
        {
            "name": "中原区",
            "is_hide": 0,
            "gid": 2198,
            "father_id": 2191,
            "users": [
                {
                    "uid": 83541,
                    "username": "care.chen"
                }
            ]
        },
        {
            "name": "华东区",
            "is_hide": 0,
            "gid": 2199,
            "father_id": 2191,
            "users": []
        },
        {
            "name": "东南区",
            "is_hide": 0,
            "gid": 2200,
            "father_id": 2191,
            "users": [
                {
                    "uid": 95806,
                    "username": "yadong.zhu"
                }
            ]
        },
        {
            "name": "华南区",
            "is_hide": 0,
            "gid": 2201,
            "father_id": 2191,
            "users": [
                {
                    "uid": 1071,
                    "username": "peter.zeng"
                }
            ]
        },
        {
            "name": "北京BP",
            "is_hide": 0,
            "gid": 154,
            "father_id": 1946,
            "users": [
                {
                    "uid": 16464,
                    "username": "cora.song"
                },
                {
                    "uid": 18283,
                    "username": "lycy.han"
                },
                {
                    "uid": 10887,
                    "username": "moon.deng"
                }
            ]
        },
        {
            "name": "中西区",
            "is_hide": 0,
            "gid": 2202,
            "father_id": 2191,
            "users": [
                {
                    "uid": 89767,
                    "username": "bigger.huang"
                }
            ]
        },
        {
            "name": "保定分公司",
            "is_hide": 0,
            "gid": 2203,
            "father_id": 2197,
            "users": [
                {
                    "uid": 739340,
                    "username": "fisker.xiao"
                },
                {
                    "uid": 746902,
                    "username": "april.liu"
                },
                {
                    "uid": 10947,
                    "username": "clare.chen"
                }
            ]
        },
        {
            "name": "临沂分公司",
            "is_hide": 0,
            "gid": 2204,
            "father_id": 2198,
            "users": []
        },
        {
            "name": "烟台分公司",
            "is_hide": 0,
            "gid": 2205,
            "father_id": 2198,
            "users": [
                {
                    "uid": 739874,
                    "username": "williamw.wang"
                },
                {
                    "uid": 740348,
                    "username": "zhang.yi"
                },
                {
                    "uid": 743349,
                    "username": "frank.gao"
                }
            ]
        },
        {
            "name": "连云港分公司",
            "is_hide": 0,
            "gid": 2206,
            "father_id": 2198,
            "users": [
                {
                    "uid": 14667,
                    "username": "arthur.fang"
                }
            ]
        },
        {
            "name": "宿迁分公司",
            "is_hide": 0,
            "gid": 2207,
            "father_id": 2198,
            "users": []
        },
        {
            "name": "淮安分公司",
            "is_hide": 0,
            "gid": 2208,
            "father_id": 2198,
            "users": [
                {
                    "uid": 744286,
                    "username": "jennifer.yan"
                },
                {
                    "uid": 14823,
                    "username": "alan.qiao"
                }
            ]
        },
        {
            "name": "盐城分公司",
            "is_hide": 0,
            "gid": 2209,
            "father_id": 2198,
            "users": []
        },
        {
            "name": "洛阳分公司",
            "is_hide": 0,
            "gid": 2210,
            "father_id": 2198,
            "users": [
                {
                    "uid": 65766,
                    "username": "archer.lei"
                },
                {
                    "uid": 742436,
                    "username": "ruoyu.liu"
                },
                {
                    "uid": 735973,
                    "username": "lahm.zhang"
                }
            ]
        },
        {
            "name": "潍坊分公司",
            "is_hide": 0,
            "gid": 2211,
            "father_id": 2198,
            "users": []
        },
        {
            "name": "芜湖分公司",
            "is_hide": 0,
            "gid": 2212,
            "father_id": 2199,
            "users": [
                {
                    "uid": 737675,
                    "username": "ant.lu"
                },
                {
                    "uid": 743253,
                    "username": "fei.ren"
                },
                {
                    "uid": 745800,
                    "username": "tom.yu"
                },
                {
                    "uid": 15312,
                    "username": "webb.wan"
                }
            ]
        },
        {
            "name": "南京BP",
            "is_hide": 0,
            "gid": 165,
            "father_id": 1944,
            "users": [
                {
                    "uid": 17941,
                    "username": "darcy.xu"
                },
                {
                    "uid": 96487,
                    "username": "gloria.zhang"
                }
            ]
        },
        {
            "name": "阜阳分公司",
            "is_hide": 0,
            "gid": 2213,
            "father_id": 2199,
            "users": [
                {
                    "uid": 15470,
                    "username": "carl.yuan"
                }
            ]
        },
        {
            "name": "泰州分公司",
            "is_hide": 0,
            "gid": 2214,
            "father_id": 2199,
            "users": []
        },
        {
            "name": "海口分公司",
            "is_hide": 0,
            "gid": 2215,
            "father_id": 2201,
            "users": [
                {
                    "uid": 65849,
                    "username": "daris.chen"
                },
                {
                    "uid": 12201,
                    "username": "sturt.wu"
                }
            ]
        },
        {
            "name": "宜昌分公司",
            "is_hide": 0,
            "gid": 2216,
            "father_id": 2202,
            "users": [
                {
                    "uid": 2129,
                    "username": "sandra.zuo"
                },
                {
                    "uid": 747087,
                    "username": "richard.wang"
                },
                {
                    "uid": 30202,
                    "username": "alan.wan"
                }
            ]
        },
        {
            "name": "遵义分公司",
            "is_hide": 0,
            "gid": 2217,
            "father_id": 2202,
            "users": []
        },
        {
            "name": "上海BP",
            "is_hide": 0,
            "gid": 170,
            "father_id": 1945,
            "users": [
                {
                    "uid": 30068,
                    "username": "jun.liu"
                },
                {
                    "uid": 15479,
                    "username": "elinazy.zhang"
                }
            ]
        },
        {
            "name": "整合营销部",
            "is_hide": 0,
            "gid": 194728,
            "father_id": 67,
            "users": [
                {
                    "uid": 65860,
                    "username": "mata.feng"
                },
                {
                    "uid": 90279,
                    "username": "ran.an"
                },
                {
                    "uid": 81426,
                    "username": "lisa.sun"
                }
            ]
        },
        {
            "name": "云设计开拓组",
            "is_hide": 0,
            "gid": 2221,
            "father_id": 1988,
            "users": [
                {
                    "uid": 56540,
                    "username": "andy.zou"
                }
            ]
        },
        {
            "name": "战狼队",
            "is_hide": 0,
            "gid": 2222,
            "father_id": 2221,
            "users": [
                {
                    "uid": 65921,
                    "username": "along.tang"
                },
                {
                    "uid": 66674,
                    "username": "bob.tang"
                },
                {
                    "uid": 1647,
                    "username": "carson.li"
                },
                {
                    "uid": 85480,
                    "username": "health.lin"
                },
                {
                    "uid": 85484,
                    "username": "gerry.tan"
                },
                {
                    "uid": 745649,
                    "username": "yao.hu"
                },
                {
                    "uid": 10581,
                    "username": "ada.ai"
                },
                {
                    "uid": 10921,
                    "username": "lulu.zhang"
                },
                {
                    "uid": 10938,
                    "username": "vincent.yuan"
                },
                {
                    "uid": 30120,
                    "username": "viking.he"
                }
            ]
        },
        {
            "name": "先锋队",
            "is_hide": 0,
            "gid": 2223,
            "father_id": 2221,
            "users": [
                {
                    "uid": 16928,
                    "username": "kirito.lu"
                },
                {
                    "uid": 66379,
                    "username": "danxia.ma"
                },
                {
                    "uid": 1681,
                    "username": "marly.ming"
                },
                {
                    "uid": 67781,
                    "username": "isaac.yang"
                },
                {
                    "uid": 56673,
                    "username": "caiyuan.jiang"
                },
                {
                    "uid": 10634,
                    "username": "light.chen"
                },
                {
                    "uid": 15386,
                    "username": "yuic.zhu"
                },
                {
                    "uid": 15565,
                    "username": "winters.tian"
                }
            ]
        },
        {
            "name": "飞跃队",
            "is_hide": 0,
            "gid": 2224,
            "father_id": 2221,
            "users": [
                {
                    "uid": 737582,
                    "username": "danae.xie"
                },
                {
                    "uid": 737584,
                    "username": "cassie.deng"
                },
                {
                    "uid": 68262,
                    "username": "frxing.fu"
                },
                {
                    "uid": 740349,
                    "username": "amanda.zhu"
                },
                {
                    "uid": 85479,
                    "username": "adah.yuan"
                },
                {
                    "uid": 741152,
                    "username": "fangbin.liang"
                },
                {
                    "uid": 742438,
                    "username": "messi.zheng"
                },
                {
                    "uid": 746917,
                    "username": "jeremy.huang"
                },
                {
                    "uid": 10074,
                    "username": "sunny.gao"
                },
                {
                    "uid": 10359,
                    "username": "aimee.yang"
                },
                {
                    "uid": 16162,
                    "username": "alan.shen"
                }
            ]
        },
        {
            "name": "尖刀队",
            "is_hide": 1,
            "gid": 2225,
            "father_id": 2221,
            "users": []
        },
        {
            "name": "狼牙队",
            "is_hide": 0,
            "gid": 2226,
            "father_id": 2221,
            "users": [
                {
                    "uid": 1570,
                    "username": "angel.ke"
                },
                {
                    "uid": 67166,
                    "username": "diy.yang"
                },
                {
                    "uid": 67212,
                    "username": "xiaoyi.zhuo"
                },
                {
                    "uid": 1685,
                    "username": "linda.wang"
                },
                {
                    "uid": 67246,
                    "username": "hai.tang"
                },
                {
                    "uid": 67782,
                    "username": "jame.yang"
                },
                {
                    "uid": 68076,
                    "username": "pacey.zhou"
                },
                {
                    "uid": 68078,
                    "username": "darius.deng"
                },
                {
                    "uid": 68090,
                    "username": "lnny.xie"
                },
                {
                    "uid": 735109,
                    "username": "vicky.wang"
                }
            ]
        },
        {
            "name": "广州分公司",
            "is_hide": 0,
            "gid": 2227,
            "father_id": 2201,
            "users": [
                {
                    "uid": 89495,
                    "username": "eric.he"
                }
            ]
        },
        {
            "name": "深圳分公司",
            "is_hide": 0,
            "gid": 2228,
            "father_id": 2201,
            "users": [
                {
                    "uid": 747225,
                    "username": "vivien.liu"
                },
                {
                    "uid": 747231,
                    "username": "bell.chen"
                }
            ]
        },
        {
            "name": "辅材运营组",
            "is_hide": 0,
            "gid": 2229,
            "father_id": 2191,
            "users": []
        },
        {
            "name": "KA运营组",
            "is_hide": 0,
            "gid": 2230,
            "father_id": 2191,
            "users": []
        },
        {
            "name": "客服中心",
            "is_hide": 0,
            "gid": 2231,
            "father_id": 0,
            "users": [
                {
                    "uid": 32,
                    "username": "eve.li"
                }
            ]
        },
        {
            "name": "产品研发部",
            "is_hide": 1,
            "gid": 2232,
            "father_id": 596,
            "users": []
        },
        {
            "name": "设计师运营组",
            "is_hide": 0,
            "gid": 2233,
            "father_id": 1659,
            "users": []
        },
        {
            "name": "流量运营组",
            "is_hide": 0,
            "gid": 2234,
            "father_id": 1659,
            "users": []
        },
        {
            "name": "薪酬管理部",
            "is_hide": 0,
            "gid": 187,
            "father_id": 3,
            "users": [
                {
                    "uid": 18180,
                    "username": "emma.liu"
                },
                {
                    "uid": 12628,
                    "username": "jean.tu"
                },
                {
                    "uid": 13614,
                    "username": "shirley.jiang"
                },
                {
                    "uid": 16009,
                    "username": "debbie.zhu"
                }
            ]
        },
        {
            "name": "协同办公组",
            "is_hide": 1,
            "gid": 2235,
            "father_id": 1542,
            "users": []
        },
        {
            "name": "人力资源组",
            "is_hide": 1,
            "gid": 2236,
            "father_id": 1542,
            "users": []
        },
        {
            "name": "财务产品组",
            "is_hide": 1,
            "gid": 2237,
            "father_id": 1661,
            "users": []
        },
        {
            "name": "结算产品组",
            "is_hide": 1,
            "gid": 2238,
            "father_id": 1661,
            "users": []
        },
        {
            "name": "配送物流组",
            "is_hide": 1,
            "gid": 2239,
            "father_id": 1604,
            "users": []
        },
        {
            "name": "仓储管理组",
            "is_hide": 1,
            "gid": 2240,
            "father_id": 1604,
            "users": []
        },
        {
            "name": "采购管理组",
            "is_hide": 1,
            "gid": 2241,
            "father_id": 1604,
            "users": []
        },
        {
            "name": "交付管理组",
            "is_hide": 1,
            "gid": 2242,
            "father_id": 1810,
            "users": []
        },
        {
            "name": "设计与即时通讯组",
            "is_hide": 1,
            "gid": 2243,
            "father_id": 1810,
            "users": []
        },
        {
            "name": "销售管理组",
            "is_hide": 1,
            "gid": 2244,
            "father_id": 1810,
            "users": []
        },
        {
            "name": "产品运营组",
            "is_hide": 1,
            "gid": 2245,
            "father_id": 1810,
            "users": []
        },
        {
            "name": "客服产品组",
            "is_hide": 1,
            "gid": 2246,
            "father_id": 2353,
            "users": []
        },
        {
            "name": "跨界商务组",
            "is_hide": 0,
            "gid": 2247,
            "father_id": 2118,
            "users": []
        },
        {
            "name": "渠道孵化组",
            "is_hide": 1,
            "gid": 2248,
            "father_id": 2118,
            "users": []
        },
        {
            "name": "新媒体组",
            "is_hide": 0,
            "gid": 2249,
            "father_id": 1623,
            "users": []
        },
        {
            "name": "争议解决组",
            "is_hide": 0,
            "gid": 2250,
            "father_id": 843,
            "users": [
                {
                    "uid": 65986,
                    "username": "vichy.wang"
                },
                {
                    "uid": 79796,
                    "username": "eiffer.li"
                }
            ]
        },
        {
            "name": "公司资本组",
            "is_hide": 0,
            "gid": 2251,
            "father_id": 843,
            "users": [
                {
                    "uid": 1330,
                    "username": "anny.shen"
                },
                {
                    "uid": 94858,
                    "username": "dian.hao"
                },
                {
                    "uid": 15767,
                    "username": "zhaoyun.yuan"
                },
                {
                    "uid": 16221,
                    "username": "may.zhu"
                }
            ]
        },
        {
            "name": "知识产权组",
            "is_hide": 0,
            "gid": 2252,
            "father_id": 843,
            "users": [
                {
                    "uid": 738745,
                    "username": "crystal.song"
                }
            ]
        },
        {
            "name": "产品定义组",
            "is_hide": 1,
            "gid": 2253,
            "father_id": 1366,
            "users": []
        },
        {
            "name": "口碑组",
            "is_hide": 0,
            "gid": 2254,
            "father_id": 1015,
            "users": [
                {
                    "uid": 16058,
                    "username": "jason.fang"
                }
            ]
        },
        {
            "name": "运营组",
            "is_hide": 0,
            "gid": 2255,
            "father_id": 1015,
            "users": [
                {
                    "uid": 15625,
                    "username": "bill.guo"
                }
            ]
        },
        {
            "name": "策略部",
            "is_hide": 1,
            "gid": 2256,
            "father_id": 2231,
            "users": []
        },
        {
            "name": "落地回访三组",
            "is_hide": 0,
            "gid": 2257,
            "father_id": 2142,
            "users": [
                {
                    "uid": 16592,
                    "username": "hiram.li"
                },
                {
                    "uid": 18105,
                    "username": "duanhan.guo"
                },
                {
                    "uid": 67785,
                    "username": "bery.zheng"
                },
                {
                    "uid": 744334,
                    "username": "vision.xu"
                },
                {
                    "uid": 56627,
                    "username": "helen.wei"
                },
                {
                    "uid": 10537,
                    "username": "nina.yang"
                },
                {
                    "uid": 11029,
                    "username": "tina.wei"
                },
                {
                    "uid": 11868,
                    "username": "jastin.jia"
                },
                {
                    "uid": 12104,
                    "username": "blue.deng"
                },
                {
                    "uid": 12320,
                    "username": "rambo.lin"
                },
                {
                    "uid": 15896,
                    "username": "ellie.peng"
                }
            ]
        },
        {
            "name": "兰州BP",
            "is_hide": 0,
            "gid": 2258,
            "father_id": 2173,
            "users": []
        },
        {
            "name": "兰州分公司",
            "is_hide": 0,
            "gid": 2259,
            "father_id": 2198,
            "users": [
                {
                    "uid": 745594,
                    "username": "xiyu.wang"
                }
            ]
        },
        {
            "name": "南区",
            "is_hide": 0,
            "gid": 2260,
            "father_id": 1352,
            "users": [
                {
                    "uid": 54,
                    "username": "kelly.zhang"
                }
            ]
        },
        {
            "name": "北区",
            "is_hide": 0,
            "gid": 2261,
            "father_id": 1352,
            "users": [
                {
                    "uid": 82,
                    "username": "joey.zhuo"
                }
            ]
        },
        {
            "name": "非落地三组",
            "is_hide": 0,
            "gid": 2262,
            "father_id": 2260,
            "users": [
                {
                    "uid": 66535,
                    "username": "smile.lv"
                },
                {
                    "uid": 66537,
                    "username": "hanber.yin"
                },
                {
                    "uid": 66536,
                    "username": "ekal.weng"
                },
                {
                    "uid": 66923,
                    "username": "burce.li"
                },
                {
                    "uid": 66924,
                    "username": "dhd.dong"
                },
                {
                    "uid": 67047,
                    "username": "yolanda.li"
                },
                {
                    "uid": 739067,
                    "username": "jingjing.yin"
                },
                {
                    "uid": 739064,
                    "username": "summer.sun"
                },
                {
                    "uid": 739069,
                    "username": "david.cao"
                },
                {
                    "uid": 739063,
                    "username": "olivia.xu"
                },
                {
                    "uid": 67569,
                    "username": "songhua.zeng"
                },
                {
                    "uid": 739339,
                    "username": "jiaxing.zhou"
                },
                {
                    "uid": 67684,
                    "username": "ziying.tang"
                },
                {
                    "uid": 739482,
                    "username": "mickey.zhang"
                },
                {
                    "uid": 740058,
                    "username": "yuan.xie"
                },
                {
                    "uid": 86175,
                    "username": "limin.wang"
                },
                {
                    "uid": 86177,
                    "username": "tayloy.huang"
                },
                {
                    "uid": 86176,
                    "username": "candy.lei"
                },
                {
                    "uid": 86179,
                    "username": "sucy.zheng"
                },
                {
                    "uid": 86178,
                    "username": "amanda.kuang"
                },
                {
                    "uid": 56665,
                    "username": "omy.ren"
                },
                {
                    "uid": 11648,
                    "username": "deigo.cheng"
                }
            ]
        },
        {
            "name": "襄阳分公司",
            "is_hide": 0,
            "gid": 2263,
            "father_id": 2202,
            "users": [
                {
                    "uid": 65858,
                    "username": "jimmy.xu"
                },
                {
                    "uid": 739464,
                    "username": "bayi.hu"
                }
            ]
        },
        {
            "name": "营销策划活动组",
            "is_hide": 0,
            "gid": 2264,
            "father_id": 2118,
            "users": []
        },
        {
            "name": "IT运维组",
            "is_hide": 1,
            "gid": 231,
            "father_id": 583,
            "users": []
        },
        {
            "name": "业务运维组",
            "is_hide": 1,
            "gid": 232,
            "father_id": 1727,
            "users": []
        },
        {
            "name": "iOS研发组",
            "is_hide": 0,
            "gid": 233,
            "father_id": 2167,
            "users": [
                {
                    "uid": 491611,
                    "username": "kris.wang"
                },
                {
                    "uid": 65826,
                    "username": "jaylan.lu"
                },
                {
                    "uid": 17314,
                    "username": "joann.hou"
                },
                {
                    "uid": 745318,
                    "username": "joakim.liu"
                },
                {
                    "uid": 12677,
                    "username": "kevin.huang"
                },
                {
                    "uid": 13470,
                    "username": "jerry.jiang"
                },
                {
                    "uid": 734773,
                    "username": "jolin.ding"
                },
                {
                    "uid": 15542,
                    "username": "kale.zhou"
                },
                {
                    "uid": 16147,
                    "username": "anyeler.zhang"
                }
            ]
        },
        {
            "name": "Andriod研发组",
            "is_hide": 0,
            "gid": 234,
            "father_id": 2167,
            "users": [
                {
                    "uid": 17461,
                    "username": "mike.gao"
                },
                {
                    "uid": 18450,
                    "username": "alvin.zhou"
                },
                {
                    "uid": 18454,
                    "username": "axl.chen"
                },
                {
                    "uid": 739465,
                    "username": "money.qian"
                },
                {
                    "uid": 740960,
                    "username": "cola.gu"
                },
                {
                    "uid": 743759,
                    "username": "aviva.tang"
                },
                {
                    "uid": 56567,
                    "username": "ying.fu"
                },
                {
                    "uid": 91503,
                    "username": "denzel.gui"
                },
                {
                    "uid": 11849,
                    "username": "young.lv"
                },
                {
                    "uid": 93881,
                    "username": "same.li"
                },
                {
                    "uid": 13487,
                    "username": "ben.hong"
                },
                {
                    "uid": 14779,
                    "username": "lew.liu"
                },
                {
                    "uid": 15416,
                    "username": "ricky.peng"
                },
                {
                    "uid": 16230,
                    "username": "mason.shang"
                }
            ]
        },
        {
            "name": "售前组",
            "is_hide": 0,
            "gid": 192750,
            "father_id": 2169,
            "users": [
                {
                    "uid": 56569,
                    "username": "roly.luo"
                },
                {
                    "uid": 56650,
                    "username": "diana.li"
                },
                {
                    "uid": 735311,
                    "username": "yue.zhang"
                },
                {
                    "uid": 14546,
                    "username": "tony.huang"
                },
                {
                    "uid": 14556,
                    "username": "springs.wu"
                },
                {
                    "uid": 15459,
                    "username": "spring.he"
                }
            ]
        },
        {
            "name": "基础平台研发组",
            "is_hide": 0,
            "gid": 192754,
            "father_id": 2168,
            "users": [
                {
                    "uid": 16310,
                    "username": "allen.yao"
                }
            ]
        },
        {
            "name": "产业研发组",
            "is_hide": 0,
            "gid": 192755,
            "father_id": 2168,
            "users": [
                {
                    "uid": 737408,
                    "username": "alan.li"
                },
                {
                    "uid": 741513,
                    "username": "yangpan.chen"
                },
                {
                    "uid": 728633,
                    "username": "terry.hao"
                },
                {
                    "uid": 30173,
                    "username": "yolanda.yu"
                },
                {
                    "uid": 735606,
                    "username": "teal.yao"
                }
            ]
        },
        {
            "name": "设计研发部",
            "is_hide": 0,
            "gid": 192758,
            "father_id": 583,
            "users": [
                {
                    "uid": 13350,
                    "username": "jerry.hu"
                }
            ]
        },
        {
            "name": "测试一组",
            "is_hide": 0,
            "gid": 192756,
            "father_id": 1896,
            "users": [
                {
                    "uid": 737535,
                    "username": "michelle.jia"
                },
                {
                    "uid": 737534,
                    "username": "xijuan.zhu"
                },
                {
                    "uid": 737536,
                    "username": "wenbin.wen"
                },
                {
                    "uid": 16769,
                    "username": "twen.wen"
                },
                {
                    "uid": 738841,
                    "username": "sf.ding"
                },
                {
                    "uid": 739613,
                    "username": "anne.lin"
                },
                {
                    "uid": 56542,
                    "username": "di.deng"
                },
                {
                    "uid": 745455,
                    "username": "stack.lin"
                },
                {
                    "uid": 747067,
                    "username": "alicea.huang"
                },
                {
                    "uid": 97129,
                    "username": "lily.xia"
                }
            ]
        },
        {
            "name": "测试二组",
            "is_hide": 0,
            "gid": 192757,
            "father_id": 1896,
            "users": [
                {
                    "uid": 16387,
                    "username": "cici.zheng"
                },
                {
                    "uid": 30028,
                    "username": "rea.xiong"
                },
                {
                    "uid": 30046,
                    "username": "charlie.peng"
                },
                {
                    "uid": 30115,
                    "username": "jin.qin"
                },
                {
                    "uid": 13931,
                    "username": "jessie.pan"
                }
            ]
        },
        {
            "name": "企业IT组",
            "is_hide": 0,
            "gid": 192762,
            "father_id": 45,
            "users": [
                {
                    "uid": 92547,
                    "username": "xander.liu"
                },
                {
                    "uid": 13327,
                    "username": "simon.ye"
                },
                {
                    "uid": 13548,
                    "username": "smile.luo"
                }
            ]
        },
        {
            "name": "业务运维组",
            "is_hide": 0,
            "gid": 192763,
            "father_id": 45,
            "users": [
                {
                    "uid": 56568,
                    "username": "vera.jiang"
                },
                {
                    "uid": 13337,
                    "username": "kui.liu"
                },
                {
                    "uid": 14926,
                    "username": "janson.jiang"
                }
            ]
        },
        {
            "name": "效能转化组",
            "is_hide": 0,
            "gid": 192766,
            "father_id": 192764,
            "users": [
                {
                    "uid": 65836,
                    "username": "wilson.wu"
                },
                {
                    "uid": 739401,
                    "username": "hugh.huang"
                },
                {
                    "uid": 88725,
                    "username": "felix.huang"
                },
                {
                    "uid": 14555,
                    "username": "swolf.lin"
                },
                {
                    "uid": 736803,
                    "username": "snow.weng"
                }
            ]
        },
        {
            "name": "落地回访四组",
            "is_hide": 0,
            "gid": 2301,
            "father_id": 2142,
            "users": [
                {
                    "uid": 1620,
                    "username": "rebecca.zeng"
                },
                {
                    "uid": 83607,
                    "username": "sasha.xiong"
                },
                {
                    "uid": 83608,
                    "username": "joker.deng"
                },
                {
                    "uid": 2027,
                    "username": "brave.chen"
                },
                {
                    "uid": 88535,
                    "username": "huiwen.fu"
                },
                {
                    "uid": 10046,
                    "username": "anby.liu"
                },
                {
                    "uid": 76156,
                    "username": "eric.ni"
                },
                {
                    "uid": 12329,
                    "username": "ben.zhu"
                },
                {
                    "uid": 80666,
                    "username": "yanny.zhang"
                }
            ]
        },
        {
            "name": "装企网店组",
            "is_hide": 0,
            "gid": 192767,
            "father_id": 192764,
            "users": [
                {
                    "uid": 1021,
                    "username": "div.xing"
                },
                {
                    "uid": 1554,
                    "username": "leo.li"
                },
                {
                    "uid": 743843,
                    "username": "austin.zheng"
                },
                {
                    "uid": 15366,
                    "username": "kris.rao"
                }
            ]
        },
        {
            "name": "清远市",
            "is_hide": 0,
            "gid": 2302,
            "father_id": 2332,
            "users": [
                {
                    "uid": 11138,
                    "username": "key.ke"
                }
            ]
        },
        {
            "name": "装企研发部",
            "is_hide": 0,
            "gid": 192764,
            "father_id": 583,
            "users": []
        },
        {
            "name": "海口市",
            "is_hide": 0,
            "gid": 2303,
            "father_id": 2332,
            "users": [
                {
                    "uid": 12417,
                    "username": "neil.liu"
                }
            ]
        },
        {
            "name": "技术工程平台组",
            "is_hide": 0,
            "gid": 192765,
            "father_id": 192768,
            "users": [
                {
                    "uid": 67061,
                    "username": "yason.li"
                },
                {
                    "uid": 67062,
                    "username": "reed.chen"
                }
            ]
        },
        {
            "name": "保定市",
            "is_hide": 0,
            "gid": 2304,
            "father_id": 2327,
            "users": [
                {
                    "uid": 12455,
                    "username": "bruce.jiao"
                }
            ]
        },
        {
            "name": "洛阳市",
            "is_hide": 0,
            "gid": 2305,
            "father_id": 2336,
            "users": [
                {
                    "uid": 14258,
                    "username": "night.liu"
                }
            ]
        },
        {
            "name": "综合支撑组",
            "is_hide": 0,
            "gid": 258,
            "father_id": 109,
            "users": [
                {
                    "uid": 17509,
                    "username": "michelle.liang"
                },
                {
                    "uid": 745304,
                    "username": "cooper.xiao"
                },
                {
                    "uid": 10076,
                    "username": "chengsi"
                },
                {
                    "uid": 747495,
                    "username": "anita.li"
                },
                {
                    "uid": 12630,
                    "username": "jack.cheng"
                },
                {
                    "uid": 14446,
                    "username": "rinky.li"
                },
                {
                    "uid": 15045,
                    "username": "chen.zhang"
                },
                {
                    "uid": 15960,
                    "username": "to8toxz"
                }
            ]
        },
        {
            "name": "淮安市",
            "is_hide": 0,
            "gid": 2306,
            "father_id": 1840,
            "users": [
                {
                    "uid": 12019,
                    "username": "cameron.du"
                }
            ]
        },
        {
            "name": "用户研发部",
            "is_hide": 0,
            "gid": 192768,
            "father_id": 583,
            "users": [
                {
                    "uid": 13347,
                    "username": "klein.li"
                }
            ]
        },
        {
            "name": "总部前台",
            "is_hide": 0,
            "gid": 259,
            "father_id": 109,
            "users": [
                {
                    "uid": 56591,
                    "username": "lym.xu"
                },
                {
                    "uid": 745382,
                    "username": "camila.xiao"
                },
                {
                    "uid": 91523,
                    "username": "jenna.zhao"
                }
            ]
        },
        {
            "name": "潍坊市",
            "is_hide": 0,
            "gid": 2307,
            "father_id": 1840,
            "users": []
        },
        {
            "name": "烟台市",
            "is_hide": 0,
            "gid": 2308,
            "father_id": 1840,
            "users": [
                {
                    "uid": 12562,
                    "username": "nydia.jing"
                }
            ]
        },
        {
            "name": "临沂市",
            "is_hide": 0,
            "gid": 2309,
            "father_id": 1840,
            "users": []
        },
        {
            "name": "连云港市",
            "is_hide": 0,
            "gid": 2310,
            "father_id": 1840,
            "users": [
                {
                    "uid": 14318,
                    "username": "jun.han"
                }
            ]
        },
        {
            "name": "未分架构",
            "is_hide": 1,
            "gid": 263,
            "father_id": 0,
            "users": []
        },
        {
            "name": "宿迁市",
            "is_hide": 0,
            "gid": 2311,
            "father_id": 1840,
            "users": []
        },
        {
            "name": "盐城市",
            "is_hide": 0,
            "gid": 2312,
            "father_id": 1840,
            "users": []
        },
        {
            "name": "芜湖市",
            "is_hide": 0,
            "gid": 2313,
            "father_id": 2329,
            "users": [
                {
                    "uid": 11455,
                    "username": "michael.li"
                }
            ]
        },
        {
            "name": "阜阳市",
            "is_hide": 0,
            "gid": 2314,
            "father_id": 2329,
            "users": [
                {
                    "uid": 1479,
                    "username": "winter.tang"
                }
            ]
        },
        {
            "name": "泰州市",
            "is_hide": 0,
            "gid": 2315,
            "father_id": 2328,
            "users": []
        },
        {
            "name": "遵义市",
            "is_hide": 0,
            "gid": 2316,
            "father_id": 2333,
            "users": []
        },
        {
            "name": "襄阳市",
            "is_hide": 0,
            "gid": 2317,
            "father_id": 2337,
            "users": [
                {
                    "uid": 11042,
                    "username": "kingkim.wu"
                }
            ]
        },
        {
            "name": "宜昌市",
            "is_hide": 0,
            "gid": 2318,
            "father_id": 2337,
            "users": [
                {
                    "uid": 10188,
                    "username": "hero.zhang"
                }
            ]
        },
        {
            "name": "售后服务部",
            "is_hide": 0,
            "gid": 2319,
            "father_id": 1926,
            "users": [
                {
                    "uid": 10671,
                    "username": "tonny.dong"
                },
                {
                    "uid": 12095,
                    "username": "boyce.wu"
                },
                {
                    "uid": 14537,
                    "username": "lokin.liu"
                }
            ]
        },
        {
            "name": "兰州市",
            "is_hide": 0,
            "gid": 2320,
            "father_id": 2336,
            "users": [
                {
                    "uid": 14313,
                    "username": "basil.li"
                }
            ]
        },
        {
            "name": "深圳市场组",
            "is_hide": 0,
            "gid": 2321,
            "father_id": 2118,
            "users": [
                {
                    "uid": 65844,
                    "username": "anni.fan"
                },
                {
                    "uid": 12444,
                    "username": "risen.li"
                },
                {
                    "uid": 14287,
                    "username": "luffy.chen"
                },
                {
                    "uid": 16346,
                    "username": "romen.wang"
                }
            ]
        },
        {
            "name": "杭宁温昌市",
            "is_hide": 0,
            "gid": 2322,
            "father_id": 2323,
            "users": []
        },
        {
            "name": "东南区",
            "is_hide": 0,
            "gid": 2323,
            "father_id": 1722,
            "users": [
                {
                    "uid": 1691,
                    "username": "xinen.chen"
                }
            ]
        },
        {
            "name": "厦泉福市",
            "is_hide": 0,
            "gid": 2324,
            "father_id": 2323,
            "users": []
        },
        {
            "name": "苏嘉市",
            "is_hide": 0,
            "gid": 2325,
            "father_id": 2323,
            "users": []
        },
        {
            "name": "大哈长市",
            "is_hide": 0,
            "gid": 2326,
            "father_id": 1837,
            "users": [
                {
                    "uid": 14162,
                    "username": "answer.li"
                }
            ]
        },
        {
            "name": "天保石太市",
            "is_hide": 0,
            "gid": 2327,
            "father_id": 1837,
            "users": []
        },
        {
            "name": "常镇泰市",
            "is_hide": 0,
            "gid": 2328,
            "father_id": 1836,
            "users": []
        },
        {
            "name": "合芜阜市",
            "is_hide": 0,
            "gid": 2329,
            "father_id": 1836,
            "users": []
        },
        {
            "name": "南通常熟市",
            "is_hide": 0,
            "gid": 2330,
            "father_id": 1836,
            "users": []
        },
        {
            "name": "莞惠赣市",
            "is_hide": 0,
            "gid": 2331,
            "father_id": 1834,
            "users": []
        },
        {
            "name": "南中海清市",
            "is_hide": 0,
            "gid": 2332,
            "father_id": 1834,
            "users": []
        },
        {
            "name": "昆贵遵市",
            "is_hide": 0,
            "gid": 2333,
            "father_id": 1829,
            "users": []
        },
        {
            "name": "长衡市",
            "is_hide": 0,
            "gid": 2334,
            "father_id": 1829,
            "users": []
        },
        {
            "name": "重绵充市",
            "is_hide": 0,
            "gid": 2335,
            "father_id": 1829,
            "users": []
        },
        {
            "name": "郑洛咸兰市",
            "is_hide": 0,
            "gid": 2336,
            "father_id": 1840,
            "users": []
        },
        {
            "name": "武襄宜市",
            "is_hide": 0,
            "gid": 2337,
            "father_id": 1829,
            "users": []
        },
        {
            "name": "客服部",
            "is_hide": 0,
            "gid": 2338,
            "father_id": 1927,
            "users": [
                {
                    "uid": 16524,
                    "username": "dora.he"
                },
                {
                    "uid": 1903,
                    "username": "candy.xu"
                },
                {
                    "uid": 14857,
                    "username": "vicky.xu"
                }
            ]
        },
        {
            "name": "广州店",
            "is_hide": 0,
            "gid": 2339,
            "father_id": 1583,
            "users": []
        },
        {
            "name": "广州设计二部",
            "is_hide": 0,
            "gid": 2340,
            "father_id": 2339,
            "users": [
                {
                    "uid": 17303,
                    "username": "jason.su"
                },
                {
                    "uid": 18008,
                    "username": "beck.dong"
                },
                {
                    "uid": 85027,
                    "username": "hongmin.huang"
                },
                {
                    "uid": 85028,
                    "username": "amber.zhang"
                },
                {
                    "uid": 90152,
                    "username": "may.he"
                }
            ]
        },
        {
            "name": "APP运营组",
            "is_hide": 0,
            "gid": 2344,
            "father_id": 195825,
            "users": [
                {
                    "uid": 16657,
                    "username": "fish.zhan"
                },
                {
                    "uid": 90727,
                    "username": "amber.liu"
                },
                {
                    "uid": 10295,
                    "username": "sach.lan"
                },
                {
                    "uid": 77290,
                    "username": "hannibal.fang"
                },
                {
                    "uid": 15150,
                    "username": "leeca.wang"
                }
            ]
        },
        {
            "name": "自媒体运营组",
            "is_hide": 0,
            "gid": 2345,
            "father_id": 195825,
            "users": [
                {
                    "uid": 16562,
                    "username": "pancy.pan"
                },
                {
                    "uid": 740965,
                    "username": "anya.wang"
                },
                {
                    "uid": 88400,
                    "username": "martin.liao"
                },
                {
                    "uid": 88724,
                    "username": "vicky.bao"
                },
                {
                    "uid": 747497,
                    "username": "astro.teng"
                },
                {
                    "uid": 15458,
                    "username": "lainey.gong"
                }
            ]
        },
        {
            "name": "新渠道开拓部",
            "is_hide": 1,
            "gid": 2346,
            "father_id": 2231,
            "users": []
        },
        {
            "name": "第三方渠道合作组",
            "is_hide": 0,
            "gid": 2347,
            "father_id": 192227,
            "users": [
                {
                    "uid": 16662,
                    "username": "maria.zhou"
                },
                {
                    "uid": 2073,
                    "username": "angelia.gu"
                },
                {
                    "uid": 84777,
                    "username": "lyn.chen"
                }
            ]
        },
        {
            "name": "运营二组",
            "is_hide": 0,
            "gid": 2348,
            "father_id": 1616,
            "users": [
                {
                    "uid": 17540,
                    "username": "pan.xu"
                },
                {
                    "uid": 83606,
                    "username": "leader.liu"
                },
                {
                    "uid": 89797,
                    "username": "shy.huang"
                },
                {
                    "uid": 92138,
                    "username": "edwin.yuan"
                },
                {
                    "uid": 92630,
                    "username": "saisai.huang"
                },
                {
                    "uid": 30167,
                    "username": "baolin.huang"
                },
                {
                    "uid": 80664,
                    "username": "snake.guo"
                },
                {
                    "uid": 15603,
                    "username": "lin.xiao"
                }
            ]
        },
        {
            "name": "BD产品组",
            "is_hide": 1,
            "gid": 2352,
            "father_id": 1810,
            "users": []
        },
        {
            "name": "供应链产品部",
            "is_hide": 0,
            "gid": 2353,
            "father_id": 1366,
            "users": [
                {
                    "uid": 16898,
                    "username": "kunlun.mou"
                },
                {
                    "uid": 17889,
                    "username": "xin.li"
                },
                {
                    "uid": 18032,
                    "username": "trayvon.huang"
                },
                {
                    "uid": 18261,
                    "username": "phoebe.guo"
                },
                {
                    "uid": 18413,
                    "username": "jinshi.liu"
                },
                {
                    "uid": 745306,
                    "username": "vincent.xiao"
                },
                {
                    "uid": 11106,
                    "username": "julia.zhao"
                }
            ]
        },
        {
            "name": "质检产品组",
            "is_hide": 1,
            "gid": 2354,
            "father_id": 2353,
            "users": []
        },
        {
            "name": "用户产品部",
            "is_hide": 0,
            "gid": 2355,
            "father_id": 1366,
            "users": [
                {
                    "uid": 16495,
                    "username": "janwin.lv"
                },
                {
                    "uid": 1036,
                    "username": "allen.wu"
                },
                {
                    "uid": 1095,
                    "username": "snow.chu"
                },
                {
                    "uid": 1227,
                    "username": "wolf.tao"
                },
                {
                    "uid": 1836,
                    "username": "fit.zhang"
                },
                {
                    "uid": 18441,
                    "username": "michael.qiao"
                },
                {
                    "uid": 743669,
                    "username": "dalton.li"
                },
                {
                    "uid": 12529,
                    "username": "barry.chen"
                },
                {
                    "uid": 30072,
                    "username": "phil.liao"
                },
                {
                    "uid": 16116,
                    "username": "focus.he"
                }
            ]
        },
        {
            "name": "业务支持部",
            "is_hide": 0,
            "gid": 2361,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "南京市",
            "is_hide": 0,
            "gid": 194968,
            "father_id": 192203,
            "users": []
        },
        {
            "name": "合肥BP",
            "is_hide": 0,
            "gid": 444,
            "father_id": 1944,
            "users": []
        },
        {
            "name": "杭州BP",
            "is_hide": 0,
            "gid": 577,
            "father_id": 1945,
            "users": [
                {
                    "uid": 15980,
                    "username": "jane.lou"
                }
            ]
        },
        {
            "name": "沈阳BP",
            "is_hide": 0,
            "gid": 578,
            "father_id": 1946,
            "users": [
                {
                    "uid": 16987,
                    "username": "baisy.chen"
                },
                {
                    "uid": 12155,
                    "username": "amy.shan"
                }
            ]
        },
        {
            "name": "昆山BP",
            "is_hide": 0,
            "gid": 579,
            "father_id": 1945,
            "users": [
                {
                    "uid": 17699,
                    "username": "jassie.wang"
                }
            ]
        },
        {
            "name": "无锡BP",
            "is_hide": 0,
            "gid": 581,
            "father_id": 1944,
            "users": []
        },
        {
            "name": "东莞BP",
            "is_hide": 0,
            "gid": 582,
            "father_id": 2174,
            "users": [
                {
                    "uid": 10139,
                    "username": "facial.mo"
                }
            ]
        },
        {
            "name": "技术研发中心",
            "is_hide": 0,
            "gid": 583,
            "father_id": 0,
            "users": [
                {
                    "uid": 1848,
                    "username": "jay.zhang"
                },
                {
                    "uid": 18265,
                    "username": "to8todev"
                },
                {
                    "uid": 10968,
                    "username": "steven.hu"
                },
                {
                    "uid": 30154,
                    "username": "data_service"
                }
            ]
        },
        {
            "name": "媒体运营组",
            "is_hide": 0,
            "gid": 588,
            "father_id": 2234,
            "users": [
                {
                    "uid": 10959,
                    "username": "cherry.zhu"
                },
                {
                    "uid": 14036,
                    "username": "jelly.zhan"
                },
                {
                    "uid": 16267,
                    "username": "zola.zhao"
                }
            ]
        },
        {
            "name": "产品组",
            "is_hide": 1,
            "gid": 589,
            "father_id": 1659,
            "users": []
        },
        {
            "name": "销售组",
            "is_hide": 0,
            "gid": 591,
            "father_id": 2233,
            "users": [
                {
                    "uid": 72,
                    "username": "rita.ouyang"
                },
                {
                    "uid": 16569,
                    "username": "daniel.huang"
                },
                {
                    "uid": 82817,
                    "username": "kerr.hu"
                },
                {
                    "uid": 85485,
                    "username": "molly.zhao"
                },
                {
                    "uid": 86428,
                    "username": "chungui.xu"
                },
                {
                    "uid": 10960,
                    "username": "melissa.wei"
                },
                {
                    "uid": 10961,
                    "username": "charlie.che"
                },
                {
                    "uid": 10985,
                    "username": "ping.zhao"
                },
                {
                    "uid": 30276,
                    "username": "shudong.ye"
                }
            ]
        },
        {
            "name": "项目组",
            "is_hide": 0,
            "gid": 592,
            "father_id": 2233,
            "users": [
                {
                    "uid": 16501,
                    "username": "linda.feng"
                },
                {
                    "uid": 1593,
                    "username": "miya.zhang"
                },
                {
                    "uid": 56549,
                    "username": "meixian.lai"
                },
                {
                    "uid": 56552,
                    "username": "xiaoyan.xu"
                },
                {
                    "uid": 10478,
                    "username": "erin.liu"
                },
                {
                    "uid": 10582,
                    "username": "chloe.zheng"
                },
                {
                    "uid": 11474,
                    "username": "loly.luo"
                },
                {
                    "uid": 11823,
                    "username": "soleil.kuang"
                },
                {
                    "uid": 30225,
                    "username": "zhile.liang"
                }
            ]
        },
        {
            "name": "3D云设计组",
            "is_hide": 1,
            "gid": 595,
            "father_id": 2232,
            "users": []
        },
        {
            "name": "云设计事业部",
            "is_hide": 1,
            "gid": 596,
            "father_id": 0,
            "users": []
        },
        {
            "name": "云设计后台组",
            "is_hide": 0,
            "gid": 597,
            "father_id": 192758,
            "users": [
                {
                    "uid": 66033,
                    "username": "terry.tang"
                },
                {
                    "uid": 17601,
                    "username": "ray.wang"
                },
                {
                    "uid": 91886,
                    "username": "ezio.xu"
                }
            ]
        },
        {
            "name": "云设计前端组",
            "is_hide": 0,
            "gid": 598,
            "father_id": 192758,
            "users": [
                {
                    "uid": 17315,
                    "username": "liangyu.chen"
                },
                {
                    "uid": 739142,
                    "username": "yee.wang"
                },
                {
                    "uid": 67422,
                    "username": "steven.shen"
                },
                {
                    "uid": 87216,
                    "username": "yuxue.huang"
                },
                {
                    "uid": 743709,
                    "username": "lan.dong"
                },
                {
                    "uid": 56655,
                    "username": "allen.qiu"
                },
                {
                    "uid": 56656,
                    "username": "andy.lin"
                },
                {
                    "uid": 91888,
                    "username": "chenghua.tang"
                },
                {
                    "uid": 736802,
                    "username": "liang.yan"
                }
            ]
        },
        {
            "name": "装企平台组",
            "is_hide": 0,
            "gid": 600,
            "father_id": 192764,
            "users": [
                {
                    "uid": 65837,
                    "username": "fisher.chen"
                },
                {
                    "uid": 743673,
                    "username": "karl.li"
                },
                {
                    "uid": 10001,
                    "username": "fsv.qing"
                },
                {
                    "uid": 732365,
                    "username": "kalen.hong"
                }
            ]
        },
        {
            "name": "客户服务部",
            "is_hide": 1,
            "gid": 603,
            "father_id": 2231,
            "users": []
        },
        {
            "name": "400接听组",
            "is_hide": 1,
            "gid": 612,
            "father_id": 1231,
            "users": []
        },
        {
            "name": "安全平台组",
            "is_hide": 0,
            "gid": 643,
            "father_id": 45,
            "users": []
        },
        {
            "name": "运营一组",
            "is_hide": 0,
            "gid": 730,
            "father_id": 1616,
            "users": [
                {
                    "uid": 737381,
                    "username": "rambo.zhang"
                },
                {
                    "uid": 1683,
                    "username": "skye.deng"
                },
                {
                    "uid": 68891,
                    "username": "whatis.liu"
                },
                {
                    "uid": 88537,
                    "username": "yinhai.gong"
                },
                {
                    "uid": 88536,
                    "username": "minty.tu"
                },
                {
                    "uid": 88853,
                    "username": "yancey.li"
                },
                {
                    "uid": 746872,
                    "username": "bernie.li"
                },
                {
                    "uid": 746870,
                    "username": "rain.ning"
                },
                {
                    "uid": 746869,
                    "username": "kerry.wan"
                },
                {
                    "uid": 746899,
                    "username": "qian.yu"
                },
                {
                    "uid": 746900,
                    "username": "lucky.xie"
                },
                {
                    "uid": 746916,
                    "username": "cole.guo"
                },
                {
                    "uid": 747341,
                    "username": "minghao.chen"
                },
                {
                    "uid": 11378,
                    "username": "sunshine.liu"
                }
            ]
        },
        {
            "name": "电商顾问扬帆组",
            "is_hide": 1,
            "gid": 731,
            "father_id": 1616,
            "users": []
        },
        {
            "name": "电商顾问魅力组",
            "is_hide": 1,
            "gid": 732,
            "father_id": 1616,
            "users": []
        },
        {
            "name": "电商顾问凌云组",
            "is_hide": 1,
            "gid": 733,
            "father_id": 1616,
            "users": []
        },
        {
            "name": "深圳市场部",
            "is_hide": 1,
            "gid": 735,
            "father_id": 1582,
            "users": []
        },
        {
            "name": "上海市场部",
            "is_hide": 0,
            "gid": 736,
            "father_id": 1576,
            "users": []
        },
        {
            "name": "北京市场组",
            "is_hide": 0,
            "gid": 737,
            "father_id": 2118,
            "users": [
                {
                    "uid": 16869,
                    "username": "gillian.wu"
                },
                {
                    "uid": 18432,
                    "username": "bend.zhang"
                },
                {
                    "uid": 85335,
                    "username": "ye.cao"
                },
                {
                    "uid": 56576,
                    "username": "alina.chen"
                },
                {
                    "uid": 56658,
                    "username": "gordon.gao"
                },
                {
                    "uid": 13553,
                    "username": "melody.huang"
                },
                {
                    "uid": 13682,
                    "username": "alan.jiang"
                },
                {
                    "uid": 30188,
                    "username": "sunny.zhai"
                },
                {
                    "uid": 15732,
                    "username": "herman.hao"
                },
                {
                    "uid": 16000,
                    "username": "fang.zhao"
                }
            ]
        },
        {
            "name": "广州市场部",
            "is_hide": 0,
            "gid": 738,
            "father_id": 2339,
            "users": [
                {
                    "uid": 82725,
                    "username": "ryan.yan"
                },
                {
                    "uid": 30090,
                    "username": "emma.pan"
                }
            ]
        },
        {
            "name": "南京市场组",
            "is_hide": 1,
            "gid": 739,
            "father_id": 2118,
            "users": []
        },
        {
            "name": "厦门市场部",
            "is_hide": 0,
            "gid": 741,
            "father_id": 1588,
            "users": []
        },
        {
            "name": "合肥市场部",
            "is_hide": 0,
            "gid": 742,
            "father_id": 1569,
            "users": []
        },
        {
            "name": "大连市场部",
            "is_hide": 0,
            "gid": 743,
            "father_id": 1573,
            "users": []
        },
        {
            "name": "苏州市场部",
            "is_hide": 0,
            "gid": 744,
            "father_id": 1568,
            "users": []
        },
        {
            "name": "创意组",
            "is_hide": 1,
            "gid": 748,
            "father_id": 67,
            "users": []
        },
        {
            "name": "公共事务部",
            "is_hide": 0,
            "gid": 749,
            "father_id": 195824,
            "users": [
                {
                    "uid": 65846,
                    "username": "dylan.ji"
                },
                {
                    "uid": 18377,
                    "username": "davide.cui"
                },
                {
                    "uid": 56602,
                    "username": "ruby.gu"
                },
                {
                    "uid": 13790,
                    "username": "suki.zhu"
                },
                {
                    "uid": 13821,
                    "username": "david.xu"
                },
                {
                    "uid": 736798,
                    "username": "wayne.qiu"
                }
            ]
        },
        {
            "name": "内容协调组",
            "is_hide": 1,
            "gid": 750,
            "father_id": 749,
            "users": []
        },
        {
            "name": "综合事务组",
            "is_hide": 1,
            "gid": 751,
            "father_id": 749,
            "users": []
        },
        {
            "name": "人才发展部",
            "is_hide": 0,
            "gid": 762,
            "father_id": 3,
            "users": [
                {
                    "uid": 13551,
                    "username": "irene.chen"
                },
                {
                    "uid": 15264,
                    "username": "gigi.huang"
                },
                {
                    "uid": 15278,
                    "username": "monica.li"
                },
                {
                    "uid": 15932,
                    "username": "carrie.yang"
                },
                {
                    "uid": 16263,
                    "username": "jason.hu"
                }
            ]
        },
        {
            "name": "腾龙组",
            "is_hide": 1,
            "gid": 764,
            "father_id": 1355,
            "users": []
        },
        {
            "name": "太阳组",
            "is_hide": 1,
            "gid": 765,
            "father_id": 1361,
            "users": []
        },
        {
            "name": "星星组",
            "is_hide": 1,
            "gid": 766,
            "father_id": 1361,
            "users": []
        },
        {
            "name": "月亮组",
            "is_hide": 1,
            "gid": 767,
            "father_id": 1363,
            "users": []
        },
        {
            "name": "孔雀组",
            "is_hide": 1,
            "gid": 768,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "锐锋组",
            "is_hide": 1,
            "gid": 769,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "火花组",
            "is_hide": 1,
            "gid": 770,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "飞扬组",
            "is_hide": 1,
            "gid": 773,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "利剑组",
            "is_hide": 1,
            "gid": 774,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "新秀组",
            "is_hide": 1,
            "gid": 775,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "闪电组",
            "is_hide": 1,
            "gid": 777,
            "father_id": 1355,
            "users": []
        },
        {
            "name": "青春组",
            "is_hide": 1,
            "gid": 778,
            "father_id": 1355,
            "users": []
        },
        {
            "name": "钻石组",
            "is_hide": 1,
            "gid": 779,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "玄鹰组",
            "is_hide": 1,
            "gid": 780,
            "father_id": 1355,
            "users": []
        },
        {
            "name": "落地回访二组",
            "is_hide": 0,
            "gid": 787,
            "father_id": 2142,
            "users": [
                {
                    "uid": 17455,
                    "username": "cinda.li"
                },
                {
                    "uid": 18104,
                    "username": "wyj.wei"
                },
                {
                    "uid": 739015,
                    "username": "kaoping.liu"
                },
                {
                    "uid": 56624,
                    "username": "guihua.liu"
                },
                {
                    "uid": 56643,
                    "username": "lillian.li"
                },
                {
                    "uid": 10356,
                    "username": "sissi.zhang"
                },
                {
                    "uid": 12197,
                    "username": "john.song"
                },
                {
                    "uid": 12200,
                    "username": "carl.liu"
                },
                {
                    "uid": 78898,
                    "username": "snow.wu"
                },
                {
                    "uid": 79826,
                    "username": "peaceful.lin"
                },
                {
                    "uid": 15248,
                    "username": "pear.wen"
                },
                {
                    "uid": 15434,
                    "username": "bess.zhou"
                }
            ]
        },
        {
            "name": "勇拓组",
            "is_hide": 1,
            "gid": 789,
            "father_id": 1362,
            "users": []
        },
        {
            "name": "飞创组",
            "is_hide": 1,
            "gid": 790,
            "father_id": 1362,
            "users": []
        },
        {
            "name": "领航组",
            "is_hide": 1,
            "gid": 791,
            "father_id": 1741,
            "users": []
        },
        {
            "name": "落地回访一组",
            "is_hide": 0,
            "gid": 792,
            "father_id": 2142,
            "users": [
                {
                    "uid": 17171,
                    "username": "dendi.xu"
                },
                {
                    "uid": 10264,
                    "username": "caroline.zhang"
                },
                {
                    "uid": 10265,
                    "username": "bin.chen"
                },
                {
                    "uid": 10345,
                    "username": "carambola.yang"
                },
                {
                    "uid": 76077,
                    "username": "world.wu"
                },
                {
                    "uid": 76080,
                    "username": "anni.hu"
                },
                {
                    "uid": 10765,
                    "username": "dudy.mo"
                },
                {
                    "uid": 10907,
                    "username": "doris.wu"
                },
                {
                    "uid": 76523,
                    "username": "chai.lin"
                },
                {
                    "uid": 11529,
                    "username": "abby.liu"
                },
                {
                    "uid": 12198,
                    "username": "helen.xiao"
                },
                {
                    "uid": 15902,
                    "username": "dorev.yang"
                }
            ]
        },
        {
            "name": "勇敢组",
            "is_hide": 1,
            "gid": 794,
            "father_id": 1361,
            "users": []
        },
        {
            "name": "腾飞组",
            "is_hide": 1,
            "gid": 795,
            "father_id": 1362,
            "users": []
        },
        {
            "name": "金刚组",
            "is_hide": 1,
            "gid": 797,
            "father_id": 1361,
            "users": []
        },
        {
            "name": "霹雳组",
            "is_hide": 1,
            "gid": 798,
            "father_id": 1361,
            "users": []
        },
        {
            "name": "阳光组",
            "is_hide": 1,
            "gid": 799,
            "father_id": 1361,
            "users": []
        },
        {
            "name": "法务部",
            "is_hide": 0,
            "gid": 843,
            "father_id": 195824,
            "users": [
                {
                    "uid": 56531,
                    "username": "joey.li"
                }
            ]
        },
        {
            "name": "厦门BP",
            "is_hide": 0,
            "gid": 844,
            "father_id": 1945,
            "users": [
                {
                    "uid": 16863,
                    "username": "anne.chen"
                }
            ]
        },
        {
            "name": "飞虎组",
            "is_hide": 1,
            "gid": 848,
            "father_id": 1355,
            "users": []
        },
        {
            "name": "城市组",
            "is_hide": 1,
            "gid": 862,
            "father_id": 1617,
            "users": []
        },
        {
            "name": "供应链与交付事业部",
            "is_hide": 1,
            "gid": 865,
            "father_id": 0,
            "users": []
        },
        {
            "name": "主材包运营中心",
            "is_hide": 1,
            "gid": 870,
            "father_id": 1736,
            "users": []
        },
        {
            "name": "预算组",
            "is_hide": 1,
            "gid": 905,
            "father_id": 907,
            "users": []
        },
        {
            "name": "城市运营组",
            "is_hide": 1,
            "gid": 906,
            "father_id": 870,
            "users": []
        },
        {
            "name": "产品研发部",
            "is_hide": 0,
            "gid": 907,
            "father_id": 1204,
            "users": [
                {
                    "uid": 16462,
                    "username": "vito.zhou"
                },
                {
                    "uid": 10697,
                    "username": "danier.wang"
                },
                {
                    "uid": 11402,
                    "username": "bee.bi"
                },
                {
                    "uid": 12527,
                    "username": "doris.li"
                },
                {
                    "uid": 14340,
                    "username": "marko.chen"
                }
            ]
        },
        {
            "name": "数据平台部",
            "is_hide": 0,
            "gid": 912,
            "father_id": 2141,
            "users": [
                {
                    "uid": 93751,
                    "username": "will.bai"
                }
            ]
        },
        {
            "name": "数据分析组",
            "is_hide": 1,
            "gid": 913,
            "father_id": 1450,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 1,
            "gid": 977,
            "father_id": 1582,
            "users": []
        },
        {
            "name": "家居顾问组",
            "is_hide": 1,
            "gid": 978,
            "father_id": 1582,
            "users": []
        },
        {
            "name": "广州设计一部",
            "is_hide": 0,
            "gid": 979,
            "father_id": 2339,
            "users": [
                {
                    "uid": 17206,
                    "username": "carrie.kuang"
                },
                {
                    "uid": 17426,
                    "username": "lian.li"
                },
                {
                    "uid": 56649,
                    "username": "ming.zhong"
                },
                {
                    "uid": 80492,
                    "username": "yuen.ruan"
                },
                {
                    "uid": 15773,
                    "username": "galen.guo"
                },
                {
                    "uid": 16228,
                    "username": "jayjo.zhang"
                }
            ]
        },
        {
            "name": "家居顾问组",
            "is_hide": 1,
            "gid": 980,
            "father_id": 1583,
            "users": []
        },
        {
            "name": "品质巡检组",
            "is_hide": 1,
            "gid": 981,
            "father_id": 1583,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 982,
            "father_id": 1584,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 983,
            "father_id": 1588,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 984,
            "father_id": 1589,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 985,
            "father_id": 1590,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 986,
            "father_id": 1575,
            "users": []
        },
        {
            "name": "家居顾问组",
            "is_hide": 0,
            "gid": 987,
            "father_id": 1575,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 988,
            "father_id": 1567,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 989,
            "father_id": 1580,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 990,
            "father_id": 1581,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 991,
            "father_id": 1578,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 992,
            "father_id": 1573,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 993,
            "father_id": 1574,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 994,
            "father_id": 1566,
            "users": []
        },
        {
            "name": "家居顾问组",
            "is_hide": 0,
            "gid": 995,
            "father_id": 1566,
            "users": []
        },
        {
            "name": "品质巡检组",
            "is_hide": 0,
            "gid": 996,
            "father_id": 1323,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 997,
            "father_id": 1569,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 998,
            "father_id": 1568,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 999,
            "father_id": 1586,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1000,
            "father_id": 1571,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1001,
            "father_id": 1570,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1002,
            "father_id": 1585,
            "users": []
        },
        {
            "name": "飞跃组",
            "is_hide": 1,
            "gid": 1003,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1004,
            "father_id": 1576,
            "users": []
        },
        {
            "name": "家居顾问组",
            "is_hide": 0,
            "gid": 1005,
            "father_id": 1576,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1006,
            "father_id": 1577,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1007,
            "father_id": 1579,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1008,
            "father_id": 1591,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1009,
            "father_id": 1592,
            "users": []
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1010,
            "father_id": 1587,
            "users": []
        },
        {
            "name": "品质巡检组",
            "is_hide": 0,
            "gid": 1013,
            "father_id": 1576,
            "users": []
        },
        {
            "name": "流量运营组",
            "is_hide": 0,
            "gid": 1015,
            "father_id": 195825,
            "users": [
                {
                    "uid": 1189,
                    "username": "xxj.xie"
                },
                {
                    "uid": 1454,
                    "username": "ryan.gong"
                }
            ]
        },
        {
            "name": "微信在线咨询组",
            "is_hide": 1,
            "gid": 1084,
            "father_id": 1231,
            "users": []
        },
        {
            "name": "测试11(0)(0)",
            "is_hide": 1,
            "gid": 1089,
            "father_id": 263,
            "users": []
        },
        {
            "name": "策士(0)",
            "is_hide": 1,
            "gid": 1090,
            "father_id": 1089,
            "users": []
        },
        {
            "name": "测试3",
            "is_hide": 1,
            "gid": 1091,
            "father_id": 1090,
            "users": []
        },
        {
            "name": "火焰队",
            "is_hide": 0,
            "gid": 1094,
            "father_id": 1615,
            "users": [
                {
                    "uid": 16923,
                    "username": "sunny.zhu"
                },
                {
                    "uid": 1061,
                    "username": "rudy.chen"
                },
                {
                    "uid": 1638,
                    "username": "little.xu"
                },
                {
                    "uid": 1968,
                    "username": "bowen.hu"
                },
                {
                    "uid": 739442,
                    "username": "xiaoen.chen"
                },
                {
                    "uid": 56608,
                    "username": "caifeng.rong"
                },
                {
                    "uid": 76062,
                    "username": "vanessa.long"
                },
                {
                    "uid": 30244,
                    "username": "guangfen.chen"
                },
                {
                    "uid": 15298,
                    "username": "vicky.zhuo"
                }
            ]
        },
        {
            "name": "卓越组",
            "is_hide": 1,
            "gid": 1095,
            "father_id": 1615,
            "users": []
        },
        {
            "name": "雪狼队",
            "is_hide": 0,
            "gid": 1096,
            "father_id": 1615,
            "users": [
                {
                    "uid": 92,
                    "username": "lolita.hua"
                },
                {
                    "uid": 1437,
                    "username": "wendy.fu"
                },
                {
                    "uid": 1643,
                    "username": "cherry.zhao"
                },
                {
                    "uid": 2117,
                    "username": "sophie.lai"
                },
                {
                    "uid": 2125,
                    "username": "alisa.sun"
                },
                {
                    "uid": 747340,
                    "username": "susu.liu"
                },
                {
                    "uid": 15520,
                    "username": "derek.liu"
                },
                {
                    "uid": 15564,
                    "username": "kevin.xiong"
                }
            ]
        },
        {
            "name": "火狼队",
            "is_hide": 0,
            "gid": 1097,
            "father_id": 1615,
            "users": [
                {
                    "uid": 1100,
                    "username": "janmy.chen"
                },
                {
                    "uid": 17793,
                    "username": "yu.zhou"
                },
                {
                    "uid": 1515,
                    "username": "angle.zhou"
                },
                {
                    "uid": 67211,
                    "username": "zhida.liu"
                },
                {
                    "uid": 1871,
                    "username": "summy.liu"
                },
                {
                    "uid": 745996,
                    "username": "fazhang.ye"
                },
                {
                    "uid": 746871,
                    "username": "davin.deng"
                },
                {
                    "uid": 747339,
                    "username": "seven.fu"
                },
                {
                    "uid": 76063,
                    "username": "gray.li"
                },
                {
                    "uid": 735953,
                    "username": "ting.huang"
                }
            ]
        },
        {
            "name": "狼牙组",
            "is_hide": 1,
            "gid": 1098,
            "father_id": 1615,
            "users": []
        },
        {
            "name": "飞鹰队",
            "is_hide": 0,
            "gid": 1099,
            "father_id": 1615,
            "users": [
                {
                    "uid": 17194,
                    "username": "jinyan.rong"
                },
                {
                    "uid": 1389,
                    "username": "nana.you"
                },
                {
                    "uid": 18098,
                    "username": "hengchao.hu"
                },
                {
                    "uid": 18256,
                    "username": "jacky.liao"
                },
                {
                    "uid": 2013,
                    "username": "beck.jiang"
                },
                {
                    "uid": 67559,
                    "username": "jiawen.zhang"
                },
                {
                    "uid": 10764,
                    "username": "spring.li"
                }
            ]
        },
        {
            "name": "众志团组",
            "is_hide": 1,
            "gid": 1100,
            "father_id": 1615,
            "users": []
        },
        {
            "name": "销售质检",
            "is_hide": 1,
            "gid": 1108,
            "father_id": 1119,
            "users": []
        },
        {
            "name": "落地审核质检",
            "is_hide": 1,
            "gid": 1109,
            "father_id": 1119,
            "users": []
        },
        {
            "name": "非落地审核质检",
            "is_hide": 1,
            "gid": 1110,
            "father_id": 1119,
            "users": []
        },
        {
            "name": "400质检",
            "is_hide": 1,
            "gid": 1111,
            "father_id": 1119,
            "users": []
        },
        {
            "name": "售前质检组",
            "is_hide": 1,
            "gid": 1112,
            "father_id": 1119,
            "users": []
        },
        {
            "name": "线上服务质检组",
            "is_hide": 1,
            "gid": 1119,
            "father_id": 1815,
            "users": []
        },
        {
            "name": "供应链管理部",
            "is_hide": 0,
            "gid": 1120,
            "father_id": 1204,
            "users": [
                {
                    "uid": 16751,
                    "username": "justin.chen"
                },
                {
                    "uid": 14421,
                    "username": "ryan.wan"
                }
            ]
        },
        {
            "name": "家居顾问组",
            "is_hide": 0,
            "gid": 1125,
            "father_id": 1568,
            "users": []
        },
        {
            "name": "秘书",
            "is_hide": 0,
            "gid": 1126,
            "father_id": 97,
            "users": [
                {
                    "uid": 30015,
                    "username": "zheng.li"
                },
                {
                    "uid": 30026,
                    "username": "iris.feng"
                }
            ]
        },
        {
            "name": "采购部",
            "is_hide": 1,
            "gid": 1127,
            "father_id": 1201,
            "users": []
        },
        {
            "name": "基建组",
            "is_hide": 0,
            "gid": 1128,
            "father_id": 109,
            "users": []
        },
        {
            "name": "HRBP运营部",
            "is_hide": 0,
            "gid": 1129,
            "father_id": 3,
            "users": []
        },
        {
            "name": "核算一部",
            "is_hide": 0,
            "gid": 1132,
            "father_id": 26,
            "users": [
                {
                    "uid": 30174,
                    "username": "amy.sun"
                }
            ]
        },
        {
            "name": "资金部",
            "is_hide": 0,
            "gid": 1133,
            "father_id": 26,
            "users": [
                {
                    "uid": 17010,
                    "username": "helen.zeng"
                },
                {
                    "uid": 1235,
                    "username": "bruce.pan"
                },
                {
                    "uid": 11223,
                    "username": "angel.tu"
                },
                {
                    "uid": 30045,
                    "username": "vivien.tang"
                },
                {
                    "uid": 30302,
                    "username": "vicki.zeng"
                },
                {
                    "uid": 14515,
                    "username": "amanda.chen"
                }
            ]
        },
        {
            "name": "费用组",
            "is_hide": 0,
            "gid": 1134,
            "father_id": 2147,
            "users": [
                {
                    "uid": 65865,
                    "username": "livi.li"
                },
                {
                    "uid": 18030,
                    "username": "jasmine.zhang"
                },
                {
                    "uid": 67423,
                    "username": "jojo.zhou"
                },
                {
                    "uid": 56613,
                    "username": "danae.zhu"
                },
                {
                    "uid": 30016,
                    "username": "charlene.zheng"
                },
                {
                    "uid": 30025,
                    "username": "claire.liu"
                }
            ]
        },
        {
            "name": "成本组",
            "is_hide": 0,
            "gid": 1135,
            "father_id": 2147,
            "users": [
                {
                    "uid": 17837,
                    "username": "gary.luo"
                },
                {
                    "uid": 18031,
                    "username": "ruyi.dai"
                },
                {
                    "uid": 18234,
                    "username": "linda.ke"
                },
                {
                    "uid": 15503,
                    "username": "zoey.li"
                }
            ]
        },
        {
            "name": "收入组",
            "is_hide": 0,
            "gid": 1136,
            "father_id": 1132,
            "users": [
                {
                    "uid": 18210,
                    "username": "rainbow.zhuang"
                },
                {
                    "uid": 10085,
                    "username": "bella.chen"
                },
                {
                    "uid": 10915,
                    "username": "cassie.fu"
                },
                {
                    "uid": 14311,
                    "username": "pandora.xu"
                }
            ]
        },
        {
            "name": "报表会计",
            "is_hide": 1,
            "gid": 1137,
            "father_id": 1132,
            "users": []
        },
        {
            "name": "计划部",
            "is_hide": 0,
            "gid": 1138,
            "father_id": 1120,
            "users": [
                {
                    "uid": 18385,
                    "username": "yanhong.lin"
                },
                {
                    "uid": 14548,
                    "username": "regan.sun"
                }
            ]
        },
        {
            "name": "结算组",
            "is_hide": 0,
            "gid": 1139,
            "father_id": 2147,
            "users": [
                {
                    "uid": 12251,
                    "username": "lily.hong"
                },
                {
                    "uid": 14437,
                    "username": "nana.luo"
                },
                {
                    "uid": 15468,
                    "username": "patty.liu"
                }
            ]
        },
        {
            "name": "招聘管理部",
            "is_hide": 0,
            "gid": 1181,
            "father_id": 3,
            "users": [
                {
                    "uid": 16528,
                    "username": "page.zhang"
                },
                {
                    "uid": 16749,
                    "username": "sky.song"
                },
                {
                    "uid": 82284,
                    "username": "tracy.liu"
                },
                {
                    "uid": 18317,
                    "username": "johnny.tang"
                },
                {
                    "uid": 18401,
                    "username": "may.mei"
                },
                {
                    "uid": 747191,
                    "username": "cony.yan"
                },
                {
                    "uid": 13805,
                    "username": "sophie.li"
                },
                {
                    "uid": 734774,
                    "username": "ellie.huang"
                },
                {
                    "uid": 13926,
                    "username": "miranda.di"
                },
                {
                    "uid": 13929,
                    "username": "ruby.zhang"
                },
                {
                    "uid": 80610,
                    "username": "alyssa.wang"
                }
            ]
        },
        {
            "name": "贵阳BP",
            "is_hide": 0,
            "gid": 1182,
            "father_id": 1947,
            "users": []
        },
        {
            "name": "郑州BP",
            "is_hide": 0,
            "gid": 1183,
            "father_id": 2173,
            "users": [
                {
                    "uid": 15977,
                    "username": "helen.wang"
                }
            ]
        },
        {
            "name": "大连BP",
            "is_hide": 0,
            "gid": 1184,
            "father_id": 1946,
            "users": [
                {
                    "uid": 14021,
                    "username": "lillian.tao"
                }
            ]
        },
        {
            "name": "苏州BP",
            "is_hide": 0,
            "gid": 1185,
            "father_id": 1945,
            "users": [
                {
                    "uid": 30132,
                    "username": "elma.liu"
                },
                {
                    "uid": 15957,
                    "username": "willie.chen"
                }
            ]
        },
        {
            "name": "西安BP",
            "is_hide": 0,
            "gid": 1186,
            "father_id": 2173,
            "users": [
                {
                    "uid": 15908,
                    "username": "ellenia.liu"
                }
            ]
        },
        {
            "name": "昆明BP",
            "is_hide": 0,
            "gid": 1187,
            "father_id": 1947,
            "users": []
        },
        {
            "name": "常州BP",
            "is_hide": 0,
            "gid": 1188,
            "father_id": 1944,
            "users": [
                {
                    "uid": 16942,
                    "username": "coffee.ding"
                }
            ]
        },
        {
            "name": "成都BP",
            "is_hide": 0,
            "gid": 1189,
            "father_id": 1947,
            "users": [
                {
                    "uid": 16974,
                    "username": "polly.zhang"
                }
            ]
        },
        {
            "name": "天津BP",
            "is_hide": 0,
            "gid": 1190,
            "father_id": 1946,
            "users": [
                {
                    "uid": 15325,
                    "username": "sunshie.zhang"
                }
            ]
        },
        {
            "name": "武汉BP",
            "is_hide": 0,
            "gid": 1191,
            "father_id": 1947,
            "users": [
                {
                    "uid": 13997,
                    "username": "shining.wang"
                }
            ]
        },
        {
            "name": "宝安",
            "is_hide": 1,
            "gid": 1192,
            "father_id": 1129,
            "users": []
        },
        {
            "name": "南宁BP",
            "is_hide": 0,
            "gid": 1193,
            "father_id": 2174,
            "users": [
                {
                    "uid": 17335,
                    "username": "sophie.wang"
                }
            ]
        },
        {
            "name": "分析预算部",
            "is_hide": 0,
            "gid": 1195,
            "father_id": 26,
            "users": [
                {
                    "uid": 65852,
                    "username": "sophia.wang"
                },
                {
                    "uid": 743172,
                    "username": "luker.lu"
                },
                {
                    "uid": 15710,
                    "username": "roger.jiang"
                }
            ]
        },
        {
            "name": "品牌设计组",
            "is_hide": 0,
            "gid": 1198,
            "father_id": 1538,
            "users": [
                {
                    "uid": 83538,
                    "username": "emily.zhou"
                },
                {
                    "uid": 84527,
                    "username": "lang.liao"
                },
                {
                    "uid": 13743,
                    "username": "dodo.du"
                },
                {
                    "uid": 735608,
                    "username": "jo.yuan"
                }
            ]
        },
        {
            "name": "视频组",
            "is_hide": 0,
            "gid": 1199,
            "father_id": 1538,
            "users": [
                {
                    "uid": 66031,
                    "username": "kara.kuang"
                },
                {
                    "uid": 88723,
                    "username": "chen.zuo"
                },
                {
                    "uid": 91508,
                    "username": "davie.chen"
                },
                {
                    "uid": 77085,
                    "username": "mia.zhou"
                },
                {
                    "uid": 30179,
                    "username": "red.wang"
                },
                {
                    "uid": 15832,
                    "username": "waston.qian"
                }
            ]
        },
        {
            "name": "监播组(0)",
            "is_hide": 1,
            "gid": 1201,
            "father_id": 1539,
            "users": []
        },
        {
            "name": "内容组",
            "is_hide": 0,
            "gid": 1202,
            "father_id": 1623,
            "users": [
                {
                    "uid": 30079,
                    "username": "shon.xiong"
                },
                {
                    "uid": 15353,
                    "username": "jason.shu"
                },
                {
                    "uid": 15754,
                    "username": "nova.zheng"
                },
                {
                    "uid": 15763,
                    "username": "nina.zhang"
                }
            ]
        },
        {
            "name": "媒介关系组",
            "is_hide": 0,
            "gid": 1203,
            "father_id": 1623,
            "users": [
                {
                    "uid": 17044,
                    "username": "jenny.zheng"
                },
                {
                    "uid": 66378,
                    "username": "deson.deng"
                },
                {
                    "uid": 30180,
                    "username": "stephanie.bo"
                },
                {
                    "uid": 15579,
                    "username": "echo.li"
                }
            ]
        },
        {
            "name": "家居建材运营中心",
            "is_hide": 0,
            "gid": 1204,
            "father_id": 0,
            "users": [
                {
                    "uid": 1029,
                    "username": "kevin.wang"
                }
            ]
        },
        {
            "name": "内容产品组",
            "is_hide": 1,
            "gid": 1224,
            "father_id": 1657,
            "users": []
        },
        {
            "name": "网页产品组",
            "is_hide": 1,
            "gid": 1225,
            "father_id": 1657,
            "users": []
        },
        {
            "name": "业主后台组",
            "is_hide": 1,
            "gid": 1226,
            "father_id": 1657,
            "users": []
        },
        {
            "name": "APP产品组",
            "is_hide": 1,
            "gid": 1227,
            "father_id": 1657,
            "users": []
        },
        {
            "name": "视觉设计组",
            "is_hide": 0,
            "gid": 1228,
            "father_id": 1657,
            "users": [
                {
                    "uid": 17772,
                    "username": "shara.lu"
                },
                {
                    "uid": 86546,
                    "username": "lyra.li"
                },
                {
                    "uid": 56574,
                    "username": "jiepin.fu"
                },
                {
                    "uid": 745437,
                    "username": "ab.chen"
                },
                {
                    "uid": 11235,
                    "username": "dean.liu"
                },
                {
                    "uid": 77169,
                    "username": "raz.fan"
                },
                {
                    "uid": 12989,
                    "username": "silvia.du"
                },
                {
                    "uid": 13515,
                    "username": "fish.xu"
                },
                {
                    "uid": 15596,
                    "username": "amy.liang"
                },
                {
                    "uid": 15621,
                    "username": "bourne.long"
                },
                {
                    "uid": 16069,
                    "username": "viki.li"
                }
            ]
        },
        {
            "name": "客诉组",
            "is_hide": 1,
            "gid": 1229,
            "father_id": 603,
            "users": []
        },
        {
            "name": "客户咨询服务部",
            "is_hide": 1,
            "gid": 1231,
            "father_id": 1815,
            "users": []
        },
        {
            "name": "物流部",
            "is_hide": 0,
            "gid": 1234,
            "father_id": 1120,
            "users": [
                {
                    "uid": 1483,
                    "username": "ares.tu"
                },
                {
                    "uid": 18360,
                    "username": "dylan.li"
                },
                {
                    "uid": 18433,
                    "username": "xu.chen"
                },
                {
                    "uid": 18435,
                    "username": "daniell.zhang"
                }
            ]
        },
        {
            "name": "家居顾问组",
            "is_hide": 0,
            "gid": 1236,
            "father_id": 1586,
            "users": []
        },
        {
            "name": "东莞运营组",
            "is_hide": 0,
            "gid": 1257,
            "father_id": 1590,
            "users": [
                {
                    "uid": 739342,
                    "username": "yingting.lian"
                },
                {
                    "uid": 739863,
                    "username": "yuchao.chen"
                },
                {
                    "uid": 10274,
                    "username": "aimee.hua"
                }
            ]
        },
        {
            "name": "福州运营组",
            "is_hide": 0,
            "gid": 1258,
            "father_id": 1589,
            "users": [
                {
                    "uid": 738800,
                    "username": "owen.jiang"
                },
                {
                    "uid": 1891,
                    "username": "jia.yu"
                }
            ]
        },
        {
            "name": "昆明运营组",
            "is_hide": 0,
            "gid": 1259,
            "father_id": 1581,
            "users": [
                {
                    "uid": 16939,
                    "username": "lime.zhang"
                },
                {
                    "uid": 17879,
                    "username": "zico.zhang"
                },
                {
                    "uid": 740888,
                    "username": "anton.sun"
                }
            ]
        },
        {
            "name": "昆山运营组",
            "is_hide": 0,
            "gid": 1260,
            "father_id": 1577,
            "users": [
                {
                    "uid": 741812,
                    "username": "tianyao.wu"
                },
                {
                    "uid": 11196,
                    "username": "jarvan.han"
                }
            ]
        },
        {
            "name": "厦门运营组",
            "is_hide": 0,
            "gid": 1261,
            "father_id": 1588,
            "users": [
                {
                    "uid": 745352,
                    "username": "zhijian.chen"
                },
                {
                    "uid": 745542,
                    "username": "ritchie.zhuang"
                },
                {
                    "uid": 746775,
                    "username": "di.zhang"
                }
            ]
        },
        {
            "name": "杭州运营组",
            "is_hide": 0,
            "gid": 1262,
            "father_id": 1579,
            "users": [
                {
                    "uid": 738097,
                    "username": "xiangjian.kong"
                },
                {
                    "uid": 17557,
                    "username": "jun.jiang"
                },
                {
                    "uid": 743893,
                    "username": "zhikun.liu"
                },
                {
                    "uid": 747334,
                    "username": "pen.ju"
                },
                {
                    "uid": 10815,
                    "username": "selina.he"
                }
            ]
        },
        {
            "name": "西安运营组",
            "is_hide": 0,
            "gid": 1263,
            "father_id": 1580,
            "users": [
                {
                    "uid": 65920,
                    "username": "fangze.shan"
                },
                {
                    "uid": 17591,
                    "username": "pag.li"
                },
                {
                    "uid": 66966,
                    "username": "jackie.yu"
                },
                {
                    "uid": 743668,
                    "username": "rex.yang"
                },
                {
                    "uid": 747397,
                    "username": "pact.liu"
                },
                {
                    "uid": 14219,
                    "username": "clark.wang"
                }
            ]
        },
        {
            "name": "成都运营组",
            "is_hide": 0,
            "gid": 1264,
            "father_id": 1592,
            "users": [
                {
                    "uid": 743548,
                    "username": "eileen.chen"
                },
                {
                    "uid": 15799,
                    "username": "vere.wei"
                },
                {
                    "uid": 16033,
                    "username": "sloane.xu"
                }
            ]
        },
        {
            "name": "合肥运营组",
            "is_hide": 0,
            "gid": 1266,
            "father_id": 1569,
            "users": [
                {
                    "uid": 1677,
                    "username": "root.qiou"
                },
                {
                    "uid": 1695,
                    "username": "yunl.xu"
                },
                {
                    "uid": 740857,
                    "username": "aiden.qian"
                },
                {
                    "uid": 742439,
                    "username": "min.pan"
                },
                {
                    "uid": 11300,
                    "username": "rex.wang"
                }
            ]
        },
        {
            "name": "公共事务中心",
            "is_hide": 0,
            "gid": 195824,
            "father_id": 0,
            "users": [
                {
                    "uid": 1052,
                    "username": "susie.xie"
                }
            ]
        },
        {
            "name": "广州运营组",
            "is_hide": 0,
            "gid": 1267,
            "father_id": 2227,
            "users": [
                {
                    "uid": 1487,
                    "username": "alisa.lu"
                },
                {
                    "uid": 740139,
                    "username": "jon.deng"
                },
                {
                    "uid": 85359,
                    "username": "andrew.zhu"
                },
                {
                    "uid": 88406,
                    "username": "mt.chen"
                },
                {
                    "uid": 15020,
                    "username": "only.wang"
                }
            ]
        },
        {
            "name": "用户运营中心",
            "is_hide": 0,
            "gid": 195825,
            "father_id": 0,
            "users": [
                {
                    "uid": 745381,
                    "username": "jammi.gu"
                }
            ]
        },
        {
            "name": "郑州运营组",
            "is_hide": 0,
            "gid": 1268,
            "father_id": 1567,
            "users": [
                {
                    "uid": 742437,
                    "username": "marker.zhang"
                },
                {
                    "uid": 743348,
                    "username": "rafael.yang"
                },
                {
                    "uid": 744285,
                    "username": "min.liang"
                },
                {
                    "uid": 10806,
                    "username": "anny.rui"
                },
                {
                    "uid": 733690,
                    "username": "ronnie.kong"
                },
                {
                    "uid": 733689,
                    "username": "lio.li"
                },
                {
                    "uid": 30258,
                    "username": "maria.zhao"
                }
            ]
        },
        {
            "name": "苏州运营组",
            "is_hide": 0,
            "gid": 1269,
            "father_id": 1568,
            "users": [
                {
                    "uid": 740858,
                    "username": "xi.chen"
                },
                {
                    "uid": 743546,
                    "username": "yan.li"
                },
                {
                    "uid": 743545,
                    "username": "genliang.guo"
                },
                {
                    "uid": 10518,
                    "username": "abel.zhang"
                }
            ]
        },
        {
            "name": "用户运营体验部",
            "is_hide": 0,
            "gid": 195831,
            "father_id": 2231,
            "users": [
                {
                    "uid": 1343,
                    "username": "juney.xiao"
                }
            ]
        },
        {
            "name": "天津运营组",
            "is_hide": 0,
            "gid": 1270,
            "father_id": 1578,
            "users": [
                {
                    "uid": 746901,
                    "username": "wakada.liang"
                },
                {
                    "uid": 11757,
                    "username": "gavin.guan"
                },
                {
                    "uid": 12407,
                    "username": "caleb.wang"
                },
                {
                    "uid": 15356,
                    "username": "fiona.guo"
                }
            ]
        },
        {
            "name": "南宁运营组",
            "is_hide": 0,
            "gid": 1271,
            "father_id": 1585,
            "users": [
                {
                    "uid": 68200,
                    "username": "arnold.xie"
                },
                {
                    "uid": 745584,
                    "username": "martin.peng"
                },
                {
                    "uid": 10504,
                    "username": "annr.liang"
                }
            ]
        },
        {
            "name": "贵阳运营组",
            "is_hide": 0,
            "gid": 1272,
            "father_id": 1587,
            "users": [
                {
                    "uid": 739865,
                    "username": "allen.ren"
                },
                {
                    "uid": 30031,
                    "username": "ai.tian"
                }
            ]
        },
        {
            "name": "佛山运营组",
            "is_hide": 0,
            "gid": 1273,
            "father_id": 1584,
            "users": [
                {
                    "uid": 741150,
                    "username": "lina.ying"
                },
                {
                    "uid": 87151,
                    "username": "kim.he"
                }
            ]
        },
        {
            "name": "统筹部",
            "is_hide": 0,
            "gid": 195835,
            "father_id": 194381,
            "users": []
        },
        {
            "name": "深圳运营组",
            "is_hide": 0,
            "gid": 1274,
            "father_id": 2228,
            "users": [
                {
                    "uid": 17324,
                    "username": "jolin.zhu"
                },
                {
                    "uid": 738743,
                    "username": "harry.wang"
                },
                {
                    "uid": 2042,
                    "username": "alana.xie"
                },
                {
                    "uid": 87142,
                    "username": "sam.du"
                },
                {
                    "uid": 745580,
                    "username": "li.yang"
                },
                {
                    "uid": 10013,
                    "username": "kandy.wang"
                },
                {
                    "uid": 30222,
                    "username": "vincent.fan"
                },
                {
                    "uid": 735605,
                    "username": "myra.huang"
                },
                {
                    "uid": 14888,
                    "username": "biby.huang"
                }
            ]
        },
        {
            "name": "区域运营部",
            "is_hide": 0,
            "gid": 195832,
            "father_id": 194381,
            "users": []
        },
        {
            "name": "无锡运营组",
            "is_hide": 0,
            "gid": 1275,
            "father_id": 1571,
            "users": [
                {
                    "uid": 18161,
                    "username": "shali.wang"
                },
                {
                    "uid": 744348,
                    "username": "maia.ma"
                },
                {
                    "uid": 745997,
                    "username": "jackie.feng"
                },
                {
                    "uid": 10021,
                    "username": "jim.hu"
                },
                {
                    "uid": 747333,
                    "username": "dolphin.gao"
                },
                {
                    "uid": 10604,
                    "username": "robin.liu"
                }
            ]
        },
        {
            "name": "南京运营组",
            "is_hide": 0,
            "gid": 1276,
            "father_id": 1566,
            "users": [
                {
                    "uid": 738744,
                    "username": "ray.chen"
                },
                {
                    "uid": 743347,
                    "username": "mary.wu"
                },
                {
                    "uid": 745302,
                    "username": "joy.jin"
                },
                {
                    "uid": 10254,
                    "username": "caesar.kon"
                },
                {
                    "uid": 15398,
                    "username": "yvonne.zhao"
                },
                {
                    "uid": 736804,
                    "username": "shine.shan"
                },
                {
                    "uid": 16099,
                    "username": "kira.liu"
                }
            ]
        },
        {
            "name": "常州运营组",
            "is_hide": 0,
            "gid": 1277,
            "father_id": 1570,
            "users": [
                {
                    "uid": 17799,
                    "username": "perrin.shen"
                },
                {
                    "uid": 735907,
                    "username": "jerry.yang"
                },
                {
                    "uid": 735905,
                    "username": "luis.zhu"
                }
            ]
        },
        {
            "name": "沈阳运营组",
            "is_hide": 0,
            "gid": 1278,
            "father_id": 1574,
            "users": [
                {
                    "uid": 11388,
                    "username": "candice.tang"
                },
                {
                    "uid": 14596,
                    "username": "john.zhao"
                }
            ]
        },
        {
            "name": "大连运营组",
            "is_hide": 0,
            "gid": 1279,
            "father_id": 1573,
            "users": [
                {
                    "uid": 737568,
                    "username": "yangyang.zhao"
                },
                {
                    "uid": 16823,
                    "username": "zebulon.ji"
                },
                {
                    "uid": 743050,
                    "username": "hao.yu"
                }
            ]
        },
        {
            "name": "小程序运营组",
            "is_hide": 0,
            "gid": 195837,
            "father_id": 195825,
            "users": [
                {
                    "uid": 65854,
                    "username": "trafford.pan"
                },
                {
                    "uid": 10014,
                    "username": "snake.zhang"
                }
            ]
        },
        {
            "name": "武汉运营组",
            "is_hide": 0,
            "gid": 1280,
            "father_id": 1591,
            "users": [
                {
                    "uid": 1491,
                    "username": "funny.wu"
                },
                {
                    "uid": 67984,
                    "username": "fei.cheng"
                },
                {
                    "uid": 739872,
                    "username": "nigel.song"
                },
                {
                    "uid": 747492,
                    "username": "fengyang.li"
                },
                {
                    "uid": 10683,
                    "username": "bella.rao"
                }
            ]
        },
        {
            "name": "长沙运营组",
            "is_hide": 0,
            "gid": 1281,
            "father_id": 1586,
            "users": [
                {
                    "uid": 65842,
                    "username": "cwen.cui"
                },
                {
                    "uid": 1730,
                    "username": "win.luo"
                },
                {
                    "uid": 746956,
                    "username": "wenxuan.kuang"
                }
            ]
        },
        {
            "name": "长沙交付部",
            "is_hide": 0,
            "gid": 1283,
            "father_id": 1586,
            "users": []
        },
        {
            "name": "郑州交付部",
            "is_hide": 0,
            "gid": 1284,
            "father_id": 1567,
            "users": []
        },
        {
            "name": "TUMAX支持组",
            "is_hide": 0,
            "gid": 195846,
            "father_id": 1985,
            "users": [
                {
                    "uid": 65863,
                    "username": "lorin.shang"
                },
                {
                    "uid": 67060,
                    "username": "helsing.ye"
                },
                {
                    "uid": 13984,
                    "username": "bill.jiang"
                },
                {
                    "uid": 96534,
                    "username": "danny.ji"
                }
            ]
        },
        {
            "name": "武汉交付部",
            "is_hide": 0,
            "gid": 1285,
            "father_id": 1591,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1286,
            "father_id": 1765,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1287,
            "father_id": 1283,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1288,
            "father_id": 1750,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1289,
            "father_id": 1284,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1290,
            "father_id": 1761,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1291,
            "father_id": 1285,
            "users": [
                {
                    "uid": 17405,
                    "username": "alison.liu"
                }
            ]
        },
        {
            "name": "业务支持组",
            "is_hide": 0,
            "gid": 195849,
            "father_id": 1985,
            "users": []
        },
        {
            "name": "北京运营组",
            "is_hide": 0,
            "gid": 1292,
            "father_id": 1575,
            "users": [
                {
                    "uid": 87157,
                    "username": "ares.du"
                },
                {
                    "uid": 87158,
                    "username": "lee.zhang"
                },
                {
                    "uid": 747287,
                    "username": "numb.zhang"
                },
                {
                    "uid": 10669,
                    "username": "dave.nie"
                },
                {
                    "uid": 11067,
                    "username": "abel.lei"
                },
                {
                    "uid": 30140,
                    "username": "jarvis.zhao"
                }
            ]
        },
        {
            "name": "上海运营组",
            "is_hide": 0,
            "gid": 1293,
            "father_id": 1576,
            "users": [
                {
                    "uid": 17114,
                    "username": "syu.zhou"
                },
                {
                    "uid": 739456,
                    "username": "luca.zeng"
                },
                {
                    "uid": 741691,
                    "username": "shore.zhang"
                },
                {
                    "uid": 744287,
                    "username": "jesy.li"
                },
                {
                    "uid": 89032,
                    "username": "winn.wang"
                },
                {
                    "uid": 745998,
                    "username": "jason.gao"
                },
                {
                    "uid": 14557,
                    "username": "fischer.chen"
                }
            ]
        },
        {
            "name": "上海交付部",
            "is_hide": 0,
            "gid": 1295,
            "father_id": 1576,
            "users": []
        },
        {
            "name": "杭州交付部",
            "is_hide": 0,
            "gid": 1296,
            "father_id": 1579,
            "users": []
        },
        {
            "name": "昆山交付部",
            "is_hide": 0,
            "gid": 1297,
            "father_id": 1577,
            "users": []
        },
        {
            "name": "上海2市",
            "is_hide": 0,
            "gid": 1298,
            "father_id": 2323,
            "users": [
                {
                    "uid": 16894,
                    "username": "xueliang.xie"
                },
                {
                    "uid": 10172,
                    "username": "bobo.tang"
                },
                {
                    "uid": 11131,
                    "username": "jun.li"
                },
                {
                    "uid": 12556,
                    "username": "sally.wang"
                },
                {
                    "uid": 12569,
                    "username": "barry.li"
                },
                {
                    "uid": 14203,
                    "username": "mckee.xu"
                },
                {
                    "uid": 14224,
                    "username": "hardy.hong"
                },
                {
                    "uid": 14402,
                    "username": "rory.ren"
                }
            ]
        },
        {
            "name": "上海3市",
            "is_hide": 0,
            "gid": 1299,
            "father_id": 2323,
            "users": [
                {
                    "uid": 1954,
                    "username": "peter.wang"
                },
                {
                    "uid": 10406,
                    "username": "arvin.wu"
                },
                {
                    "uid": 10784,
                    "username": "young.liu"
                },
                {
                    "uid": 11188,
                    "username": "gideon.yang"
                },
                {
                    "uid": 11246,
                    "username": "rudy.cheng"
                },
                {
                    "uid": 12342,
                    "username": "federer.yan"
                },
                {
                    "uid": 12563,
                    "username": "albert.zhang"
                }
            ]
        },
        {
            "name": "B检C组",
            "is_hide": 1,
            "gid": 1300,
            "father_id": 1763,
            "users": []
        },
        {
            "name": "B检D组",
            "is_hide": 1,
            "gid": 1301,
            "father_id": 1763,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1302,
            "father_id": 1295,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1303,
            "father_id": 1295,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1304,
            "father_id": 1771,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1305,
            "father_id": 1296,
            "users": [
                {
                    "uid": 17435,
                    "username": "mei.hong"
                }
            ]
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1306,
            "father_id": 1773,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1307,
            "father_id": 1297,
            "users": []
        },
        {
            "name": "APP推广组",
            "is_hide": 0,
            "gid": 195865,
            "father_id": 192227,
            "users": [
                {
                    "uid": 15336,
                    "username": "derrick.pan"
                }
            ]
        },
        {
            "name": "天津交付部",
            "is_hide": 0,
            "gid": 1309,
            "father_id": 1578,
            "users": []
        },
        {
            "name": "大连交付部",
            "is_hide": 0,
            "gid": 1310,
            "father_id": 1573,
            "users": []
        },
        {
            "name": "沈阳交付部",
            "is_hide": 0,
            "gid": 1311,
            "father_id": 1574,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1312,
            "father_id": 1760,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1313,
            "father_id": 1751,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1314,
            "father_id": 1772,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1315,
            "father_id": 1309,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1316,
            "father_id": 1310,
            "users": [
                {
                    "uid": 17152,
                    "username": "vera.xu"
                }
            ]
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1317,
            "father_id": 1311,
            "users": []
        },
        {
            "name": "常州交付部",
            "is_hide": 0,
            "gid": 1319,
            "father_id": 1570,
            "users": []
        },
        {
            "name": "无锡交付部",
            "is_hide": 0,
            "gid": 1320,
            "father_id": 1571,
            "users": []
        },
        {
            "name": "苏州交付部",
            "is_hide": 0,
            "gid": 1321,
            "father_id": 1568,
            "users": []
        },
        {
            "name": "合肥交付部",
            "is_hide": 0,
            "gid": 1322,
            "father_id": 1569,
            "users": []
        },
        {
            "name": "南京交付部",
            "is_hide": 0,
            "gid": 1323,
            "father_id": 1566,
            "users": []
        },
        {
            "name": "长沙BP",
            "is_hide": 0,
            "gid": 1324,
            "father_id": 1947,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1325,
            "father_id": 1746,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1326,
            "father_id": 1319,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1327,
            "father_id": 1774,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1328,
            "father_id": 1320,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1329,
            "father_id": 1320,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1330,
            "father_id": 1753,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1331,
            "father_id": 1321,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1332,
            "father_id": 1767,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1333,
            "father_id": 1322,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1334,
            "father_id": 1322,
            "users": []
        },
        {
            "name": "B检A组",
            "is_hide": 1,
            "gid": 1335,
            "father_id": 1758,
            "users": []
        },
        {
            "name": "B检B组",
            "is_hide": 1,
            "gid": 1336,
            "father_id": 1758,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1337,
            "father_id": 1323,
            "users": []
        },
        {
            "name": "成都交付部",
            "is_hide": 0,
            "gid": 1339,
            "father_id": 1592,
            "users": []
        },
        {
            "name": "贵阳交付部",
            "is_hide": 0,
            "gid": 1340,
            "father_id": 1587,
            "users": []
        },
        {
            "name": "西安交付部",
            "is_hide": 0,
            "gid": 1341,
            "father_id": 1580,
            "users": []
        },
        {
            "name": "昆明交付部",
            "is_hide": 0,
            "gid": 1342,
            "father_id": 1581,
            "users": []
        },
        {
            "name": "B检B组",
            "is_hide": 1,
            "gid": 1343,
            "father_id": 1747,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1344,
            "father_id": 1339,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1345,
            "father_id": 1339,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1346,
            "father_id": 1749,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1347,
            "father_id": 1340,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1348,
            "father_id": 1755,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1349,
            "father_id": 1341,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1350,
            "father_id": 1756,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1351,
            "father_id": 1342,
            "users": []
        },
        {
            "name": "审核转化部",
            "is_hide": 0,
            "gid": 1352,
            "father_id": 2231,
            "users": []
        },
        {
            "name": "落地审核",
            "is_hide": 1,
            "gid": 1353,
            "father_id": 1352,
            "users": []
        },
        {
            "name": "非落地审核",
            "is_hide": 1,
            "gid": 1355,
            "father_id": 1352,
            "users": []
        },
        {
            "name": "全程管家部",
            "is_hide": 1,
            "gid": 1356,
            "father_id": 603,
            "users": []
        },
        {
            "name": "宇宙组",
            "is_hide": 1,
            "gid": 1357,
            "father_id": 1741,
            "users": []
        },
        {
            "name": "精英组",
            "is_hide": 1,
            "gid": 1358,
            "father_id": 1356,
            "users": []
        },
        {
            "name": "商品装修管家",
            "is_hide": 1,
            "gid": 1359,
            "father_id": 1356,
            "users": []
        },
        {
            "name": "客服中心",
            "is_hide": 1,
            "gid": 1360,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "装模装中客服部",
            "is_hide": 0,
            "gid": 1361,
            "father_id": 2231,
            "users": [
                {
                    "uid": 737382,
                    "username": "anna.peng"
                },
                {
                    "uid": 17380,
                    "username": "dan.chen"
                },
                {
                    "uid": 17451,
                    "username": "kernel.pang"
                },
                {
                    "uid": 1680,
                    "username": "ken.zhang"
                },
                {
                    "uid": 18421,
                    "username": "andy.qu"
                },
                {
                    "uid": 740943,
                    "username": "yvette.li"
                },
                {
                    "uid": 743079,
                    "username": "wing.xu"
                },
                {
                    "uid": 10855,
                    "username": "cassie.huang"
                },
                {
                    "uid": 10856,
                    "username": "doreen.zhang"
                },
                {
                    "uid": 11501,
                    "username": "tina.luo"
                },
                {
                    "uid": 14426,
                    "username": "susann.lu"
                }
            ]
        },
        {
            "name": "装前回访部",
            "is_hide": 1,
            "gid": 1362,
            "father_id": 1360,
            "users": []
        },
        {
            "name": "售后服务部",
            "is_hide": 1,
            "gid": 1363,
            "father_id": 603,
            "users": []
        },
        {
            "name": "产品中心",
            "is_hide": 0,
            "gid": 1366,
            "father_id": 0,
            "users": [
                {
                    "uid": 93213,
                    "username": "douglas.wu"
                }
            ]
        },
        {
            "name": "IT支持中心",
            "is_hide": 1,
            "gid": 1367,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "工程调度组",
            "is_hide": 1,
            "gid": 1370,
            "father_id": 1366,
            "users": []
        },
        {
            "name": "问答组",
            "is_hide": 0,
            "gid": 1378,
            "father_id": 1015,
            "users": [
                {
                    "uid": 16920,
                    "username": "yilia.yan"
                },
                {
                    "uid": 18011,
                    "username": "shemy.xie"
                },
                {
                    "uid": 18097,
                    "username": "aki.yu"
                },
                {
                    "uid": 1840,
                    "username": "laura.lu"
                },
                {
                    "uid": 11152,
                    "username": "cheryl.wu"
                },
                {
                    "uid": 15597,
                    "username": "angela.chen"
                },
                {
                    "uid": 15600,
                    "username": "arlence.luo"
                }
            ]
        },
        {
            "name": "图片组",
            "is_hide": 1,
            "gid": 1379,
            "father_id": 1015,
            "users": []
        },
        {
            "name": "文章组",
            "is_hide": 0,
            "gid": 1380,
            "father_id": 1015,
            "users": []
        },
        {
            "name": "广州交付部",
            "is_hide": 0,
            "gid": 1384,
            "father_id": 1583,
            "users": []
        },
        {
            "name": "佛山交付部",
            "is_hide": 0,
            "gid": 1385,
            "father_id": 1584,
            "users": []
        },
        {
            "name": "南宁交付部",
            "is_hide": 0,
            "gid": 1386,
            "father_id": 1585,
            "users": []
        },
        {
            "name": "厦门交付部",
            "is_hide": 0,
            "gid": 1387,
            "father_id": 1588,
            "users": []
        },
        {
            "name": "福州交付部",
            "is_hide": 0,
            "gid": 1388,
            "father_id": 1589,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1389,
            "father_id": 1748,
            "users": []
        },
        {
            "name": "B检B组",
            "is_hide": 1,
            "gid": 1390,
            "father_id": 1748,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1391,
            "father_id": 1384,
            "users": [
                {
                    "uid": 17353,
                    "username": "john.guan"
                },
                {
                    "uid": 17549,
                    "username": "aaron.peng"
                },
                {
                    "uid": 11111,
                    "username": "asa.wu"
                },
                {
                    "uid": 12503,
                    "username": "bill.fan"
                },
                {
                    "uid": 14294,
                    "username": "sean.shen"
                }
            ]
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1392,
            "father_id": 1384,
            "users": [
                {
                    "uid": 12591,
                    "username": "heo.qiu"
                },
                {
                    "uid": 30204,
                    "username": "aviva.liu"
                }
            ]
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1393,
            "father_id": 1769,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1394,
            "father_id": 1385,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1395,
            "father_id": 1762,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1396,
            "father_id": 1386,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1397,
            "father_id": 1777,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1398,
            "father_id": 1387,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1399,
            "father_id": 1768,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1400,
            "father_id": 1388,
            "users": []
        },
        {
            "name": "基础架构部",
            "is_hide": 0,
            "gid": 1401,
            "father_id": 583,
            "users": [
                {
                    "uid": 83536,
                    "username": "johnny.chen"
                },
                {
                    "uid": 18452,
                    "username": "tim.wei"
                },
                {
                    "uid": 18453,
                    "username": "nigel.wang"
                },
                {
                    "uid": 11367,
                    "username": "dave.cao"
                },
                {
                    "uid": 732366,
                    "username": "cheny.huang"
                },
                {
                    "uid": 30014,
                    "username": "senix.liu"
                },
                {
                    "uid": 30093,
                    "username": "pete.wang"
                },
                {
                    "uid": 735310,
                    "username": "keith.huang"
                },
                {
                    "uid": 16314,
                    "username": "clay.zhao"
                }
            ]
        },
        {
            "name": "呼叫系统部",
            "is_hide": 1,
            "gid": 1402,
            "father_id": 583,
            "users": []
        },
        {
            "name": "企业IT部",
            "is_hide": 1,
            "gid": 1403,
            "father_id": 1727,
            "users": []
        },
        {
            "name": "移动部",
            "is_hide": 1,
            "gid": 1404,
            "father_id": 1727,
            "users": []
        },
        {
            "name": "平台研发部",
            "is_hide": 1,
            "gid": 1405,
            "father_id": 1727,
            "users": []
        },
        {
            "name": "用户研发组",
            "is_hide": 0,
            "gid": 1407,
            "father_id": 2168,
            "users": [
                {
                    "uid": 17345,
                    "username": "jiangyin.su"
                },
                {
                    "uid": 18459,
                    "username": "adams.li"
                },
                {
                    "uid": 741515,
                    "username": "erin.xiang"
                },
                {
                    "uid": 745353,
                    "username": "jack.luo"
                },
                {
                    "uid": 12509,
                    "username": "lewis.liu"
                },
                {
                    "uid": 13406,
                    "username": "hyolee.wang"
                },
                {
                    "uid": 13980,
                    "username": "tracy.xu"
                },
                {
                    "uid": 14064,
                    "username": "hank.lan"
                },
                {
                    "uid": 16048,
                    "username": "fidermo.hu"
                }
            ]
        },
        {
            "name": "后台服务组",
            "is_hide": 1,
            "gid": 1408,
            "father_id": 583,
            "users": []
        },
        {
            "name": "WEB框架组",
            "is_hide": 1,
            "gid": 1409,
            "father_id": 583,
            "users": []
        },
        {
            "name": "产品组",
            "is_hide": 1,
            "gid": 1410,
            "father_id": 1401,
            "users": []
        },
        {
            "name": "链路组",
            "is_hide": 1,
            "gid": 1411,
            "father_id": 1402,
            "users": []
        },
        {
            "name": "设计师研发组",
            "is_hide": 0,
            "gid": 1413,
            "father_id": 192758,
            "users": [
                {
                    "uid": 17015,
                    "username": "rebirth.huang"
                },
                {
                    "uid": 18442,
                    "username": "watson.zeng"
                },
                {
                    "uid": 13467,
                    "username": "reson.dai"
                },
                {
                    "uid": 14304,
                    "username": "crispan.chen"
                },
                {
                    "uid": 14569,
                    "username": "liya.liu"
                }
            ]
        },
        {
            "name": "BOSS平台组",
            "is_hide": 1,
            "gid": 1414,
            "father_id": 2168,
            "users": []
        },
        {
            "name": "用户平台组",
            "is_hide": 0,
            "gid": 1415,
            "father_id": 192768,
            "users": [
                {
                    "uid": 739463,
                    "username": "beck.liu"
                },
                {
                    "uid": 10262,
                    "username": "steven.zhang"
                }
            ]
        },
        {
            "name": "流量平台组",
            "is_hide": 0,
            "gid": 1416,
            "father_id": 192768,
            "users": [
                {
                    "uid": 741514,
                    "username": "juntao.guo"
                },
                {
                    "uid": 13237,
                    "username": "andy.xiang"
                },
                {
                    "uid": 13594,
                    "username": "wenbing.yi"
                },
                {
                    "uid": 16309,
                    "username": "seven.yuan"
                }
            ]
        },
        {
            "name": "深圳分公司",
            "is_hide": 1,
            "gid": 1424,
            "father_id": 1732,
            "users": []
        },
        {
            "name": "东莞交付部",
            "is_hide": 0,
            "gid": 1425,
            "father_id": 1590,
            "users": []
        },
        {
            "name": "B检A组",
            "is_hide": 1,
            "gid": 1426,
            "father_id": 1770,
            "users": []
        },
        {
            "name": "B检B组",
            "is_hide": 1,
            "gid": 1427,
            "father_id": 1770,
            "users": []
        },
        {
            "name": "B检C组",
            "is_hide": 1,
            "gid": 1428,
            "father_id": 1770,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 1,
            "gid": 1429,
            "father_id": 1926,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1430,
            "father_id": 1926,
            "users": [
                {
                    "uid": 17142,
                    "username": "lili.yi"
                },
                {
                    "uid": 17217,
                    "username": "maddy.zhou"
                },
                {
                    "uid": 10294,
                    "username": "kiki.xu"
                }
            ]
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1431,
            "father_id": 1926,
            "users": [
                {
                    "uid": 16910,
                    "username": "yilia.li"
                },
                {
                    "uid": 10016,
                    "username": "lucky.hu"
                },
                {
                    "uid": 11492,
                    "username": "joue.liao"
                },
                {
                    "uid": 30287,
                    "username": "youny.yang"
                },
                {
                    "uid": 30293,
                    "username": "dason.dai"
                },
                {
                    "uid": 14481,
                    "username": "stephanie.shan"
                }
            ]
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1432,
            "father_id": 1775,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1433,
            "father_id": 1425,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1434,
            "father_id": 1425,
            "users": [
                {
                    "uid": 17004,
                    "username": "betty.deng"
                },
                {
                    "uid": 30089,
                    "username": "jennifer.zhang"
                }
            ]
        },
        {
            "name": "北京交付部",
            "is_hide": 0,
            "gid": 1436,
            "father_id": 1575,
            "users": [
                {
                    "uid": 16636,
                    "username": "devin.lu"
                }
            ]
        },
        {
            "name": "北京1市",
            "is_hide": 0,
            "gid": 1437,
            "father_id": 1837,
            "users": [
                {
                    "uid": 1559,
                    "username": "amos.wei"
                },
                {
                    "uid": 10344,
                    "username": "baron.wen"
                },
                {
                    "uid": 11015,
                    "username": "sachin.wu"
                },
                {
                    "uid": 12597,
                    "username": "rainbow.tao"
                },
                {
                    "uid": 14234,
                    "username": "joye.guo"
                },
                {
                    "uid": 14270,
                    "username": "augus.zhang"
                },
                {
                    "uid": 14303,
                    "username": "glenn.liu"
                },
                {
                    "uid": 14325,
                    "username": "eric.tian"
                },
                {
                    "uid": 14383,
                    "username": "bob.zhang"
                }
            ]
        },
        {
            "name": "B检B组",
            "is_hide": 1,
            "gid": 1438,
            "father_id": 1744,
            "users": []
        },
        {
            "name": "北京2市",
            "is_hide": 0,
            "gid": 1439,
            "father_id": 1837,
            "users": [
                {
                    "uid": 17054,
                    "username": "alvin.zhao"
                },
                {
                    "uid": 17298,
                    "username": "felix.yang"
                },
                {
                    "uid": 76014,
                    "username": "jian.sun"
                },
                {
                    "uid": 11335,
                    "username": "byron.zhu"
                },
                {
                    "uid": 11386,
                    "username": "arvin.zhang"
                },
                {
                    "uid": 11962,
                    "username": "asa.wang"
                },
                {
                    "uid": 11976,
                    "username": "augus.ma"
                },
                {
                    "uid": 12515,
                    "username": "clark.li"
                },
                {
                    "uid": 14140,
                    "username": "vincent.li"
                },
                {
                    "uid": 14142,
                    "username": "jerry.wang"
                },
                {
                    "uid": 14165,
                    "username": "jeremy.cheng"
                }
            ]
        },
        {
            "name": "B检D组",
            "is_hide": 1,
            "gid": 1440,
            "father_id": 1744,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1441,
            "father_id": 1436,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1442,
            "father_id": 1436,
            "users": []
        },
        {
            "name": "交付二部",
            "is_hide": 0,
            "gid": 1443,
            "father_id": 1436,
            "users": []
        },
        {
            "name": "交付三部",
            "is_hide": 0,
            "gid": 1444,
            "father_id": 1436,
            "users": []
        },
        {
            "name": "智能家居平台事业部",
            "is_hide": 0,
            "gid": 1445,
            "father_id": 0,
            "users": [
                {
                    "uid": 16655,
                    "username": "like.zhou"
                }
            ]
        },
        {
            "name": "研发部",
            "is_hide": 0,
            "gid": 1446,
            "father_id": 1445,
            "users": []
        },
        {
            "name": "嵌入式研发组",
            "is_hide": 0,
            "gid": 1447,
            "father_id": 1446,
            "users": [
                {
                    "uid": 16904,
                    "username": "wen.yang"
                },
                {
                    "uid": 17932,
                    "username": "brook.wang"
                },
                {
                    "uid": 17933,
                    "username": "kevon.shi"
                },
                {
                    "uid": 56653,
                    "username": "eson.li"
                },
                {
                    "uid": 30081,
                    "username": "taiyi.wei"
                },
                {
                    "uid": 15424,
                    "username": "thomas.tang"
                },
                {
                    "uid": 15497,
                    "username": "william.lan"
                },
                {
                    "uid": 16223,
                    "username": "loren.li"
                }
            ]
        },
        {
            "name": "数据分析部",
            "is_hide": 0,
            "gid": 1450,
            "father_id": 2141,
            "users": [
                {
                    "uid": 16704,
                    "username": "eric.luo"
                },
                {
                    "uid": 1663,
                    "username": "canny.huang"
                },
                {
                    "uid": 89374,
                    "username": "ella.pan"
                },
                {
                    "uid": 728632,
                    "username": "luson.liu"
                },
                {
                    "uid": 92753,
                    "username": "amyx.li"
                },
                {
                    "uid": 78273,
                    "username": "julia.luo"
                },
                {
                    "uid": 733691,
                    "username": "aidan.ye"
                }
            ]
        },
        {
            "name": "数据反馈组",
            "is_hide": 1,
            "gid": 1453,
            "father_id": 1367,
            "users": []
        },
        {
            "name": "骄阳组",
            "is_hide": 1,
            "gid": 1456,
            "father_id": 1356,
            "users": []
        },
        {
            "name": "成都市场部",
            "is_hide": 0,
            "gid": 1457,
            "father_id": 1592,
            "users": []
        },
        {
            "name": "长沙市场部",
            "is_hide": 0,
            "gid": 1467,
            "father_id": 1586,
            "users": []
        },
        {
            "name": "嵌入式硬件",
            "is_hide": 1,
            "gid": 1468,
            "father_id": 1446,
            "users": []
        },
        {
            "name": "移动组",
            "is_hide": 0,
            "gid": 1469,
            "father_id": 1446,
            "users": []
        },
        {
            "name": "云后台",
            "is_hide": 0,
            "gid": 1470,
            "father_id": 1446,
            "users": []
        },
        {
            "name": "行业合作组",
            "is_hide": 1,
            "gid": 1471,
            "father_id": 1446,
            "users": []
        },
        {
            "name": "产品组",
            "is_hide": 0,
            "gid": 1472,
            "father_id": 1446,
            "users": [
                {
                    "uid": 18353,
                    "username": "steven.ma"
                },
                {
                    "uid": 56532,
                    "username": "jackx.wang"
                },
                {
                    "uid": 30125,
                    "username": "zaker.li"
                }
            ]
        },
        {
            "name": "企划销售部",
            "is_hide": 0,
            "gid": 1473,
            "father_id": 1445,
            "users": [
                {
                    "uid": 68287,
                    "username": "swallow.zeng"
                },
                {
                    "uid": 68288,
                    "username": "jasone.hu"
                },
                {
                    "uid": 56516,
                    "username": "andy.xu"
                }
            ]
        },
        {
            "name": "热火队",
            "is_hide": 1,
            "gid": 1497,
            "father_id": 1361,
            "users": []
        },
        {
            "name": "奇迹队",
            "is_hide": 1,
            "gid": 1498,
            "father_id": 1816,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1501,
            "father_id": 1311,
            "users": []
        },
        {
            "name": "重庆运营组",
            "is_hide": 0,
            "gid": 1502,
            "father_id": 1650,
            "users": [
                {
                    "uid": 89796,
                    "username": "arno.yang"
                },
                {
                    "uid": 735838,
                    "username": "tt.he"
                },
                {
                    "uid": 735956,
                    "username": "rachel.xing"
                },
                {
                    "uid": 736151,
                    "username": "rich.li"
                }
            ]
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1533,
            "father_id": 1323,
            "users": []
        },
        {
            "name": "重庆交付部",
            "is_hide": 0,
            "gid": 1534,
            "father_id": 1650,
            "users": []
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1535,
            "father_id": 1776,
            "users": []
        },
        {
            "name": "品牌部",
            "is_hide": 0,
            "gid": 1538,
            "father_id": 67,
            "users": []
        },
        {
            "name": "媒介部",
            "is_hide": 0,
            "gid": 1539,
            "father_id": 67,
            "users": [
                {
                    "uid": 12687,
                    "username": "sandy.zhou"
                },
                {
                    "uid": 14526,
                    "username": "grace.hu"
                }
            ]
        },
        {
            "name": "新媒体部",
            "is_hide": 1,
            "gid": 1540,
            "father_id": 1622,
            "users": []
        },
        {
            "name": "品牌全案组",
            "is_hide": 0,
            "gid": 1541,
            "father_id": 1538,
            "users": [
                {
                    "uid": 15962,
                    "username": "woosa.wu"
                }
            ]
        },
        {
            "name": "人力与办公产品组",
            "is_hide": 1,
            "gid": 1542,
            "father_id": 1661,
            "users": []
        },
        {
            "name": "福州BP",
            "is_hide": 0,
            "gid": 1544,
            "father_id": 1945,
            "users": []
        },
        {
            "name": "佛山BP",
            "is_hide": 0,
            "gid": 1545,
            "father_id": 2174,
            "users": []
        },
        {
            "name": "华夏组",
            "is_hide": 1,
            "gid": 1547,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "向钱组",
            "is_hide": 1,
            "gid": 1549,
            "father_id": 1363,
            "users": []
        },
        {
            "name": "商城组",
            "is_hide": 1,
            "gid": 1550,
            "father_id": 1617,
            "users": []
        },
        {
            "name": "辅材采购组",
            "is_hide": 0,
            "gid": 194066,
            "father_id": 1856,
            "users": []
        },
        {
            "name": "业务支持组",
            "is_hide": 0,
            "gid": 194065,
            "father_id": 1856,
            "users": [
                {
                    "uid": 10877,
                    "username": "coco.wei"
                },
                {
                    "uid": 11707,
                    "username": "morgan.huang"
                },
                {
                    "uid": 14954,
                    "username": "hedy.ye"
                }
            ]
        },
        {
            "name": "物流组",
            "is_hide": 0,
            "gid": 194068,
            "father_id": 1856,
            "users": []
        },
        {
            "name": "深圳BP",
            "is_hide": 0,
            "gid": 1561,
            "father_id": 2054,
            "users": [
                {
                    "uid": 13709,
                    "username": "richard.he"
                }
            ]
        },
        {
            "name": "辅材运营组",
            "is_hide": 0,
            "gid": 194075,
            "father_id": 1856,
            "users": []
        },
        {
            "name": "宝安行政组",
            "is_hide": 0,
            "gid": 1563,
            "father_id": 109,
            "users": [
                {
                    "uid": 56533,
                    "username": "carol.hu"
                },
                {
                    "uid": 13018,
                    "username": "tim.pan"
                },
                {
                    "uid": 13685,
                    "username": "anda.hu"
                },
                {
                    "uid": 13686,
                    "username": "tom.tu"
                }
            ]
        },
        {
            "name": "华东区",
            "is_hide": 0,
            "gid": 194078,
            "father_id": 194075,
            "users": [
                {
                    "uid": 747496,
                    "username": "allen.zhi"
                }
            ]
        },
        {
            "name": "中西区",
            "is_hide": 0,
            "gid": 194079,
            "father_id": 194075,
            "users": [
                {
                    "uid": 14389,
                    "username": "david.yuan"
                },
                {
                    "uid": 14918,
                    "username": "jack.ruan"
                }
            ]
        },
        {
            "name": "南京分公司",
            "is_hide": 0,
            "gid": 1566,
            "father_id": 2199,
            "users": [
                {
                    "uid": 1338,
                    "username": "cjz.chen"
                }
            ]
        },
        {
            "name": "华北区",
            "is_hide": 0,
            "gid": 194076,
            "father_id": 194075,
            "users": [
                {
                    "uid": 16357,
                    "username": "tom.hou"
                }
            ]
        },
        {
            "name": "郑州分公司",
            "is_hide": 0,
            "gid": 1567,
            "father_id": 2198,
            "users": [
                {
                    "uid": 738801,
                    "username": "super.chen"
                }
            ]
        },
        {
            "name": "中原区",
            "is_hide": 0,
            "gid": 194077,
            "father_id": 194075,
            "users": []
        },
        {
            "name": "苏州分公司",
            "is_hide": 0,
            "gid": 1568,
            "father_id": 2200,
            "users": [
                {
                    "uid": 1166,
                    "username": "paul.wu"
                }
            ]
        },
        {
            "name": "合肥分公司",
            "is_hide": 0,
            "gid": 1569,
            "father_id": 2199,
            "users": [
                {
                    "uid": 1105,
                    "username": "scott.shu"
                }
            ]
        },
        {
            "name": "常州分公司",
            "is_hide": 0,
            "gid": 1570,
            "father_id": 2199,
            "users": [
                {
                    "uid": 1363,
                    "username": "kxing.cheng"
                }
            ]
        },
        {
            "name": "无锡分公司",
            "is_hide": 0,
            "gid": 1571,
            "father_id": 2199,
            "users": [
                {
                    "uid": 736193,
                    "username": "lu.liu"
                }
            ]
        },
        {
            "name": "大连分公司",
            "is_hide": 0,
            "gid": 1573,
            "father_id": 2197,
            "users": []
        },
        {
            "name": "沈阳分公司",
            "is_hide": 0,
            "gid": 1574,
            "father_id": 2197,
            "users": [
                {
                    "uid": 15730,
                    "username": "stone.wang"
                }
            ]
        },
        {
            "name": "北京分公司",
            "is_hide": 0,
            "gid": 1575,
            "father_id": 2197,
            "users": [
                {
                    "uid": 1109,
                    "username": "buddy.zhang"
                }
            ]
        },
        {
            "name": "上海分公司",
            "is_hide": 0,
            "gid": 1576,
            "father_id": 2200,
            "users": [
                {
                    "uid": 1514,
                    "username": "john.chen"
                }
            ]
        },
        {
            "name": "华南区",
            "is_hide": 0,
            "gid": 194090,
            "father_id": 194075,
            "users": [
                {
                    "uid": 14946,
                    "username": "ada.jie"
                }
            ]
        },
        {
            "name": "昆山分公司",
            "is_hide": 0,
            "gid": 1577,
            "father_id": 2200,
            "users": []
        },
        {
            "name": "天津分公司",
            "is_hide": 0,
            "gid": 1578,
            "father_id": 2197,
            "users": [
                {
                    "uid": 1418,
                    "username": "dickson.feng"
                }
            ]
        },
        {
            "name": "杭州分公司",
            "is_hide": 0,
            "gid": 1579,
            "father_id": 2200,
            "users": [
                {
                    "uid": 740944,
                    "username": "lior.li"
                }
            ]
        },
        {
            "name": "东南区",
            "is_hide": 0,
            "gid": 194089,
            "father_id": 194075,
            "users": []
        },
        {
            "name": "西安分公司",
            "is_hide": 0,
            "gid": 1580,
            "father_id": 2198,
            "users": [
                {
                    "uid": 18376,
                    "username": "vic.liu"
                }
            ]
        },
        {
            "name": "昆明分公司",
            "is_hide": 0,
            "gid": 1581,
            "father_id": 2202,
            "users": [
                {
                    "uid": 70,
                    "username": "seven.zhang"
                }
            ]
        },
        {
            "name": "全屋定制部",
            "is_hide": 0,
            "gid": 194095,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "标准化深圳分公司",
            "is_hide": 0,
            "gid": 1582,
            "father_id": 6,
            "users": [
                {
                    "uid": 15352,
                    "username": "xing.zeng"
                }
            ]
        },
        {
            "name": "标准化广州分公司",
            "is_hide": 0,
            "gid": 1583,
            "father_id": 6,
            "users": [
                {
                    "uid": 17304,
                    "username": "sarah.pang"
                }
            ]
        },
        {
            "name": "佛山分公司",
            "is_hide": 0,
            "gid": 1584,
            "father_id": 2201,
            "users": [
                {
                    "uid": 1587,
                    "username": "cyan.hou"
                }
            ]
        },
        {
            "name": "项目运营部",
            "is_hide": 0,
            "gid": 194098,
            "father_id": 194095,
            "users": [
                {
                    "uid": 745305,
                    "username": "yiyi.deng"
                }
            ]
        },
        {
            "name": "南宁分公司",
            "is_hide": 0,
            "gid": 1585,
            "father_id": 2201,
            "users": [
                {
                    "uid": 1104,
                    "username": "kyle.chen"
                }
            ]
        },
        {
            "name": "长沙分公司",
            "is_hide": 0,
            "gid": 1586,
            "father_id": 2202,
            "users": [
                {
                    "uid": 19,
                    "username": "andy.jiang"
                }
            ]
        },
        {
            "name": "招商部",
            "is_hide": 0,
            "gid": 194096,
            "father_id": 194095,
            "users": [
                {
                    "uid": 65984,
                    "username": "eric.chen"
                },
                {
                    "uid": 2147,
                    "username": "poet.dong"
                },
                {
                    "uid": 12302,
                    "username": "susana.xie"
                },
                {
                    "uid": 14198,
                    "username": "eric.yan"
                }
            ]
        },
        {
            "name": "贵阳分公司",
            "is_hide": 0,
            "gid": 1587,
            "father_id": 2202,
            "users": [
                {
                    "uid": 1092,
                    "username": "edward.chen"
                },
                {
                    "uid": 743100,
                    "username": "smart.yao"
                }
            ]
        },
        {
            "name": "运营部",
            "is_hide": 0,
            "gid": 194097,
            "father_id": 194095,
            "users": [
                {
                    "uid": 17596,
                    "username": "arron.li"
                },
                {
                    "uid": 745581,
                    "username": "maggie.pan"
                },
                {
                    "uid": 15628,
                    "username": "fiona.wei"
                }
            ]
        },
        {
            "name": "厦门分公司",
            "is_hide": 0,
            "gid": 1588,
            "father_id": 2200,
            "users": [
                {
                    "uid": 1493,
                    "username": "jack.huang"
                }
            ]
        },
        {
            "name": "福州分公司",
            "is_hide": 0,
            "gid": 1589,
            "father_id": 2200,
            "users": [
                {
                    "uid": 1782,
                    "username": "leo.tu"
                }
            ]
        },
        {
            "name": "东莞分公司",
            "is_hide": 0,
            "gid": 1590,
            "father_id": 2201,
            "users": [
                {
                    "uid": 93,
                    "username": "dylan.chen"
                }
            ]
        },
        {
            "name": "武汉分公司",
            "is_hide": 0,
            "gid": 1591,
            "father_id": 2202,
            "users": [
                {
                    "uid": 1539,
                    "username": "durant.qiu"
                }
            ]
        },
        {
            "name": "成都分公司",
            "is_hide": 0,
            "gid": 1592,
            "father_id": 2202,
            "users": [
                {
                    "uid": 1175,
                    "username": "steven.jiang"
                }
            ]
        },
        {
            "name": "标准产品采购组",
            "is_hide": 1,
            "gid": 1593,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "定制产品采购组",
            "is_hide": 1,
            "gid": 1594,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "供应商管理部",
            "is_hide": 1,
            "gid": 1595,
            "father_id": 1120,
            "users": []
        },
        {
            "name": "辅材开拓组",
            "is_hide": 0,
            "gid": 194110,
            "father_id": 1856,
            "users": []
        },
        {
            "name": "售前产品组",
            "is_hide": 1,
            "gid": 1602,
            "father_id": 1366,
            "users": []
        },
        {
            "name": "装模业务组",
            "is_hide": 1,
            "gid": 1603,
            "father_id": 1366,
            "users": []
        },
        {
            "name": "供应链产品组",
            "is_hide": 1,
            "gid": 1604,
            "father_id": 2353,
            "users": []
        },
        {
            "name": "建材施工产品组",
            "is_hide": 1,
            "gid": 1605,
            "father_id": 1366,
            "users": []
        },
        {
            "name": "SEO技术组",
            "is_hide": 1,
            "gid": 1606,
            "father_id": 1015,
            "users": []
        },
        {
            "name": "产品运营组",
            "is_hide": 1,
            "gid": 1607,
            "father_id": 1015,
            "users": []
        },
        {
            "name": "产品组",
            "is_hide": 1,
            "gid": 1608,
            "father_id": 1015,
            "users": []
        },
        {
            "name": "装企发展中心",
            "is_hide": 0,
            "gid": 1609,
            "father_id": 0,
            "users": [
                {
                    "uid": 56539,
                    "username": "david.guo"
                }
            ]
        },
        {
            "name": "华东一区",
            "is_hide": 1,
            "gid": 1611,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "华北一区",
            "is_hide": 1,
            "gid": 1612,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "华南二区",
            "is_hide": 1,
            "gid": 1613,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "华南一区",
            "is_hide": 1,
            "gid": 1614,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "非落地开拓一组",
            "is_hide": 0,
            "gid": 1615,
            "father_id": 1988,
            "users": []
        },
        {
            "name": "非落地运营组",
            "is_hide": 0,
            "gid": 1616,
            "father_id": 1988,
            "users": []
        },
        {
            "name": "商城组",
            "is_hide": 1,
            "gid": 1617,
            "father_id": 1015,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1618,
            "father_id": 1283,
            "users": []
        },
        {
            "name": "开拓组",
            "is_hide": 1,
            "gid": 1619,
            "father_id": 1355,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1620,
            "father_id": 1319,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1621,
            "father_id": 1385,
            "users": []
        },
        {
            "name": "品牌与传播中心",
            "is_hide": 1,
            "gid": 1622,
            "father_id": 0,
            "users": []
        },
        {
            "name": "公关部",
            "is_hide": 0,
            "gid": 1623,
            "father_id": 67,
            "users": []
        },
        {
            "name": "市场推广中心",
            "is_hide": 1,
            "gid": 1624,
            "father_id": 1622,
            "users": []
        },
        {
            "name": "付费推广组",
            "is_hide": 0,
            "gid": 1625,
            "father_id": 192227,
            "users": [
                {
                    "uid": 65855,
                    "username": "leon.tang"
                },
                {
                    "uid": 1485,
                    "username": "don.tu"
                },
                {
                    "uid": 1942,
                    "username": "leaky.chen"
                },
                {
                    "uid": 743395,
                    "username": "eason.wang"
                },
                {
                    "uid": 56590,
                    "username": "lacy.li"
                },
                {
                    "uid": 11219,
                    "username": "anthony.wang"
                },
                {
                    "uid": 11225,
                    "username": "sily.huang"
                },
                {
                    "uid": 11227,
                    "username": "plaimao.huang"
                },
                {
                    "uid": 11691,
                    "username": "cici.ma"
                },
                {
                    "uid": 30226,
                    "username": "vio.lin"
                }
            ]
        },
        {
            "name": "APP与微信推广部",
            "is_hide": 1,
            "gid": 1626,
            "father_id": 1656,
            "users": []
        },
        {
            "name": "APP与微信推广部",
            "is_hide": 1,
            "gid": 1627,
            "father_id": 1655,
            "users": []
        },
        {
            "name": "商城运营组",
            "is_hide": 0,
            "gid": 1628,
            "father_id": 1659,
            "users": [
                {
                    "uid": 1771,
                    "username": "robot.luo"
                },
                {
                    "uid": 10895,
                    "username": "hope.lai"
                }
            ]
        },
        {
            "name": "广告变现组",
            "is_hide": 1,
            "gid": 1629,
            "father_id": 2346,
            "users": []
        },
        {
            "name": "落地城市一线",
            "is_hide": 1,
            "gid": 1630,
            "father_id": 1625,
            "users": []
        },
        {
            "name": "落地城市二线",
            "is_hide": 1,
            "gid": 1631,
            "father_id": 1625,
            "users": []
        },
        {
            "name": "落地城市三线",
            "is_hide": 1,
            "gid": 1632,
            "father_id": 1625,
            "users": []
        },
        {
            "name": "非落地城市",
            "is_hide": 1,
            "gid": 1633,
            "father_id": 1625,
            "users": []
        },
        {
            "name": "公共支持组",
            "is_hide": 1,
            "gid": 1634,
            "father_id": 1625,
            "users": []
        },
        {
            "name": "数据监控组",
            "is_hide": 1,
            "gid": 1635,
            "father_id": 1625,
            "users": []
        },
        {
            "name": "信息流专项组",
            "is_hide": 1,
            "gid": 1636,
            "father_id": 1625,
            "users": []
        },
        {
            "name": "拓展一组",
            "is_hide": 1,
            "gid": 1637,
            "father_id": 1626,
            "users": []
        },
        {
            "name": "拓展二组",
            "is_hide": 1,
            "gid": 1638,
            "father_id": 1626,
            "users": []
        },
        {
            "name": "APP专项组",
            "is_hide": 1,
            "gid": 1639,
            "father_id": 1626,
            "users": []
        },
        {
            "name": "邮件组",
            "is_hide": 1,
            "gid": 1640,
            "father_id": 1627,
            "users": []
        },
        {
            "name": "延期组",
            "is_hide": 1,
            "gid": 1641,
            "father_id": 1627,
            "users": []
        },
        {
            "name": "微信组",
            "is_hide": 1,
            "gid": 1645,
            "father_id": 1623,
            "users": []
        },
        {
            "name": "策划组",
            "is_hide": 1,
            "gid": 1646,
            "father_id": 1623,
            "users": []
        },
        {
            "name": "整装事业部",
            "is_hide": 1,
            "gid": 1647,
            "father_id": 0,
            "users": []
        },
        {
            "name": "重庆BP",
            "is_hide": 0,
            "gid": 1648,
            "father_id": 1947,
            "users": [
                {
                    "uid": 18350,
                    "username": "sherry.zhang"
                }
            ]
        },
        {
            "name": "广州分公司",
            "is_hide": 1,
            "gid": 1649,
            "father_id": 1133,
            "users": []
        },
        {
            "name": "重庆分公司",
            "is_hide": 0,
            "gid": 1650,
            "father_id": 2202,
            "users": [
                {
                    "uid": 103,
                    "username": "darren.feng"
                }
            ]
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1651,
            "father_id": 1534,
            "users": [
                {
                    "uid": 17724,
                    "username": "vivi.lan"
                }
            ]
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1654,
            "father_id": 1650,
            "users": []
        },
        {
            "name": "用户产品中心",
            "is_hide": 1,
            "gid": 1655,
            "father_id": 0,
            "users": []
        },
        {
            "name": "互联网推广中心",
            "is_hide": 1,
            "gid": 1656,
            "father_id": 1655,
            "users": []
        },
        {
            "name": "产品设计部",
            "is_hide": 0,
            "gid": 1657,
            "father_id": 1366,
            "users": []
        },
        {
            "name": "天马行空组",
            "is_hide": 1,
            "gid": 1658,
            "father_id": 1353,
            "users": []
        },
        {
            "name": "家居运营部",
            "is_hide": 0,
            "gid": 1659,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "金融开放平台事业部",
            "is_hide": 0,
            "gid": 1660,
            "father_id": 0,
            "users": [
                {
                    "uid": 2082,
                    "username": "funny.wei"
                },
                {
                    "uid": 2132,
                    "username": "ivan.lu"
                },
                {
                    "uid": 90725,
                    "username": "chris.dong"
                },
                {
                    "uid": 92502,
                    "username": "josephe.wu"
                },
                {
                    "uid": 732363,
                    "username": "lin.sun"
                }
            ]
        },
        {
            "name": "财经产品部",
            "is_hide": 0,
            "gid": 1661,
            "father_id": 1366,
            "users": [
                {
                    "uid": 17950,
                    "username": "trm.wang"
                },
                {
                    "uid": 18211,
                    "username": "zhengyin.deng"
                },
                {
                    "uid": 18446,
                    "username": "ruby.peng"
                },
                {
                    "uid": 68232,
                    "username": "songwen.li"
                },
                {
                    "uid": 11365,
                    "username": "vee.xu"
                },
                {
                    "uid": 16142,
                    "username": "wenting.liu"
                },
                {
                    "uid": 16305,
                    "username": "gino.dong"
                }
            ]
        },
        {
            "name": "系统产品组",
            "is_hide": 1,
            "gid": 1662,
            "father_id": 583,
            "users": []
        },
        {
            "name": "3D产品组",
            "is_hide": 1,
            "gid": 1663,
            "father_id": 2232,
            "users": []
        },
        {
            "name": "平台研发部",
            "is_hide": 1,
            "gid": 1664,
            "father_id": 583,
            "users": []
        },
        {
            "name": "运营研发部",
            "is_hide": 1,
            "gid": 1665,
            "father_id": 583,
            "users": []
        },
        {
            "name": "工人系统组",
            "is_hide": 1,
            "gid": 1666,
            "father_id": 583,
            "users": []
        },
        {
            "name": "供应链系统组",
            "is_hide": 0,
            "gid": 1667,
            "father_id": 2169,
            "users": [
                {
                    "uid": 65839,
                    "username": "bojack.hu"
                },
                {
                    "uid": 65840,
                    "username": "yilia.an"
                },
                {
                    "uid": 745319,
                    "username": "imp.zhang"
                },
                {
                    "uid": 745423,
                    "username": "don.xue"
                },
                {
                    "uid": 13307,
                    "username": "tomy.li"
                },
                {
                    "uid": 13729,
                    "username": "marko.liu"
                },
                {
                    "uid": 734772,
                    "username": "robert.zhang"
                },
                {
                    "uid": 16312,
                    "username": "trista.zhou"
                }
            ]
        },
        {
            "name": "财经研发组",
            "is_hide": 0,
            "gid": 1668,
            "father_id": 2169,
            "users": [
                {
                    "uid": 65838,
                    "username": "benjamin.zhai"
                },
                {
                    "uid": 56652,
                    "username": "jade.huang"
                },
                {
                    "uid": 30177,
                    "username": "luke.lv"
                },
                {
                    "uid": 14466,
                    "username": "damon.wu"
                },
                {
                    "uid": 16319,
                    "username": "word.huo"
                }
            ]
        },
        {
            "name": "CRM开发组",
            "is_hide": 1,
            "gid": 1669,
            "father_id": 583,
            "users": []
        },
        {
            "name": "自动呼叫开发组",
            "is_hide": 1,
            "gid": 1670,
            "father_id": 583,
            "users": []
        },
        {
            "name": "装修流程前端组",
            "is_hide": 0,
            "gid": 1671,
            "father_id": 2169,
            "users": [
                {
                    "uid": 16400,
                    "username": "gusu.zhou"
                },
                {
                    "uid": 16566,
                    "username": "zifary.lei"
                },
                {
                    "uid": 1355,
                    "username": "alex.wang"
                },
                {
                    "uid": 740869,
                    "username": "amber.guo"
                },
                {
                    "uid": 56651,
                    "username": "dinosaur.liu"
                },
                {
                    "uid": 747066,
                    "username": "cong.huang"
                },
                {
                    "uid": 14059,
                    "username": "tony.tang"
                },
                {
                    "uid": 15415,
                    "username": "jenny.wang"
                }
            ]
        },
        {
            "name": "微信运营组",
            "is_hide": 0,
            "gid": 1673,
            "father_id": 195825,
            "users": [
                {
                    "uid": 82222,
                    "username": "eva.wen"
                },
                {
                    "uid": 2008,
                    "username": "toria.zheng"
                },
                {
                    "uid": 741457,
                    "username": "lucyy.wang"
                },
                {
                    "uid": 743082,
                    "username": "vanilla.dai"
                },
                {
                    "uid": 30150,
                    "username": "joan.lin"
                },
                {
                    "uid": 30303,
                    "username": "clara.chen"
                },
                {
                    "uid": 15987,
                    "username": "jenny.liang"
                }
            ]
        },
        {
            "name": "狼牙组",
            "is_hide": 1,
            "gid": 1674,
            "father_id": 1355,
            "users": []
        },
        {
            "name": "测试组",
            "is_hide": 1,
            "gid": 1675,
            "father_id": 1366,
            "users": []
        },
        {
            "name": "客源拓展组",
            "is_hide": 0,
            "gid": 1676,
            "father_id": 2118,
            "users": [
                {
                    "uid": 16790,
                    "username": "timmy.li"
                },
                {
                    "uid": 16819,
                    "username": "helen.huang"
                },
                {
                    "uid": 1086,
                    "username": "jeff.wen"
                },
                {
                    "uid": 10023,
                    "username": "jason.wen"
                },
                {
                    "uid": 10626,
                    "username": "xiangkai.tu"
                },
                {
                    "uid": 11340,
                    "username": "devin.guo"
                },
                {
                    "uid": 14462,
                    "username": "sen.guo"
                },
                {
                    "uid": 14988,
                    "username": "lucina.zhou"
                },
                {
                    "uid": 16288,
                    "username": "annabelle.sheng"
                }
            ]
        },
        {
            "name": "装修公司模式",
            "is_hide": 1,
            "gid": 1678,
            "father_id": 1133,
            "users": []
        },
        {
            "name": "工长模式",
            "is_hide": 1,
            "gid": 1679,
            "father_id": 1133,
            "users": []
        },
        {
            "name": "主材包模式",
            "is_hide": 1,
            "gid": 1680,
            "father_id": 1133,
            "users": []
        },
        {
            "name": "出纳",
            "is_hide": 1,
            "gid": 1681,
            "father_id": 1133,
            "users": []
        },
        {
            "name": "深圳分公司",
            "is_hide": 1,
            "gid": 1682,
            "father_id": 1133,
            "users": []
        },
        {
            "name": "电商顾问勇敢组",
            "is_hide": 1,
            "gid": 1683,
            "father_id": 1616,
            "users": []
        },
        {
            "name": "先行者",
            "is_hide": 1,
            "gid": 1684,
            "father_id": 1676,
            "users": []
        },
        {
            "name": "火麒麟",
            "is_hide": 1,
            "gid": 1685,
            "father_id": 1676,
            "users": []
        },
        {
            "name": "东莞市场部",
            "is_hide": 0,
            "gid": 1687,
            "father_id": 1590,
            "users": []
        },
        {
            "name": "南宁市场部",
            "is_hide": 0,
            "gid": 1688,
            "father_id": 1585,
            "users": []
        },
        {
            "name": "服务大厅",
            "is_hide": 0,
            "gid": 1690,
            "father_id": 0,
            "users": [
                {
                    "uid": 18444,
                    "username": "dayin"
                },
                {
                    "uid": 87533,
                    "username": "1000"
                },
                {
                    "uid": 87537,
                    "username": "2000"
                },
                {
                    "uid": 87539,
                    "username": "3000"
                },
                {
                    "uid": 87541,
                    "username": "5000"
                },
                {
                    "uid": 87540,
                    "username": "4000"
                },
                {
                    "uid": 87542,
                    "username": "6000"
                },
                {
                    "uid": 88167,
                    "username": "testteam"
                },
                {
                    "uid": 94328,
                    "username": "8000"
                },
                {
                    "uid": 735782,
                    "username": "9000"
                }
            ]
        },
        {
            "name": "意见处理中心",
            "is_hide": 1,
            "gid": 1691,
            "father_id": 97,
            "users": []
        },
        {
            "name": "福州市场部",
            "is_hide": 0,
            "gid": 1692,
            "father_id": 1589,
            "users": []
        },
        {
            "name": "交付四部",
            "is_hide": 0,
            "gid": 1693,
            "father_id": 1436,
            "users": [
                {
                    "uid": 18189,
                    "username": "darcy.pan"
                },
                {
                    "uid": 12517,
                    "username": "murray.geng"
                },
                {
                    "uid": 14207,
                    "username": "alan.guan"
                }
            ]
        },
        {
            "name": "上海分公司",
            "is_hide": 1,
            "gid": 1694,
            "father_id": 1133,
            "users": []
        },
        {
            "name": "品牌维护组",
            "is_hide": 1,
            "gid": 1696,
            "father_id": 1015,
            "users": []
        },
        {
            "name": "运营组",
            "is_hide": 1,
            "gid": 1697,
            "father_id": 1617,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1698,
            "father_id": 1310,
            "users": []
        },
        {
            "name": "质量管理部",
            "is_hide": 0,
            "gid": 1701,
            "father_id": 1445,
            "users": [
                {
                    "uid": 17203,
                    "username": "beney.shen"
                },
                {
                    "uid": 18304,
                    "username": "allen.she"
                },
                {
                    "uid": 30010,
                    "username": "alice.yuan"
                },
                {
                    "uid": 30178,
                    "username": "hogan.liang"
                }
            ]
        },
        {
            "name": "制造部",
            "is_hide": 0,
            "gid": 1705,
            "father_id": 1445,
            "users": [
                {
                    "uid": 17269,
                    "username": "abel.xiong"
                },
                {
                    "uid": 17731,
                    "username": "tongs.chang"
                }
            ]
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1707,
            "father_id": 1341,
            "users": []
        },
        {
            "name": "税务组",
            "is_hide": 0,
            "gid": 1720,
            "father_id": 1132,
            "users": [
                {
                    "uid": 17045,
                    "username": "may.ma"
                },
                {
                    "uid": 17981,
                    "username": "yuanyuan.chen"
                },
                {
                    "uid": 15700,
                    "username": "victorial.tian"
                },
                {
                    "uid": 16266,
                    "username": "amanda.han"
                }
            ]
        },
        {
            "name": "项目财务部",
            "is_hide": 0,
            "gid": 1721,
            "father_id": 26,
            "users": []
        },
        {
            "name": "质检部",
            "is_hide": 0,
            "gid": 1722,
            "father_id": 194381,
            "users": [
                {
                    "uid": 1347,
                    "username": "ken.nieh"
                }
            ]
        },
        {
            "name": "基础技术中心",
            "is_hide": 1,
            "gid": 1727,
            "father_id": 7,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1728,
            "father_id": 1927,
            "users": [
                {
                    "uid": 18457,
                    "username": "haiqing.sun"
                },
                {
                    "uid": 15251,
                    "username": "rose.guan"
                }
            ]
        },
        {
            "name": "交付部",
            "is_hide": 1,
            "gid": 1729,
            "father_id": 1860,
            "users": []
        },
        {
            "name": "安装部",
            "is_hide": 0,
            "gid": 1730,
            "father_id": 1927,
            "users": [
                {
                    "uid": 30097,
                    "username": "river.lei"
                },
                {
                    "uid": 15363,
                    "username": "lusa.lu"
                }
            ]
        },
        {
            "name": "产业部",
            "is_hide": 1,
            "gid": 1731,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "分公司交付系统",
            "is_hide": 1,
            "gid": 1732,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "HRBP",
            "is_hide": 1,
            "gid": 1733,
            "father_id": 865,
            "users": []
        },
        {
            "name": "市场营销部",
            "is_hide": 1,
            "gid": 1734,
            "father_id": 6,
            "users": []
        },
        {
            "name": "客户服务部",
            "is_hide": 1,
            "gid": 1735,
            "father_id": 1985,
            "users": []
        },
        {
            "name": "店面运营部",
            "is_hide": 1,
            "gid": 1736,
            "father_id": 1734,
            "users": []
        },
        {
            "name": "数据仓库部",
            "is_hide": 0,
            "gid": 192202,
            "father_id": 2141,
            "users": [
                {
                    "uid": 89415,
                    "username": "richard.luo"
                },
                {
                    "uid": 728841,
                    "username": "richard.chen"
                },
                {
                    "uid": 15493,
                    "username": "lincoln.hao"
                }
            ]
        },
        {
            "name": "企划部",
            "is_hide": 1,
            "gid": 1737,
            "father_id": 1734,
            "users": []
        },
        {
            "name": "售后服务组",
            "is_hide": 0,
            "gid": 192203,
            "father_id": 1722,
            "users": [
                {
                    "uid": 1446,
                    "username": "andi.li"
                }
            ]
        },
        {
            "name": "市场营销开拓部",
            "is_hide": 1,
            "gid": 1738,
            "father_id": 1734,
            "users": []
        },
        {
            "name": "总部市场组",
            "is_hide": 1,
            "gid": 1739,
            "father_id": 1738,
            "users": []
        },
        {
            "name": "BD组",
            "is_hide": 1,
            "gid": 1740,
            "father_id": 1738,
            "users": []
        },
        {
            "name": "东莞市",
            "is_hide": 0,
            "gid": 192206,
            "father_id": 192203,
            "users": [
                {
                    "uid": 1334,
                    "username": "success.hua"
                }
            ]
        },
        {
            "name": "客服组",
            "is_hide": 1,
            "gid": 1741,
            "father_id": 1735,
            "users": []
        },
        {
            "name": "佛山市",
            "is_hide": 0,
            "gid": 192207,
            "father_id": 192203,
            "users": []
        },
        {
            "name": "监察组",
            "is_hide": 1,
            "gid": 1742,
            "father_id": 1735,
            "users": []
        },
        {
            "name": "杭州市",
            "is_hide": 0,
            "gid": 192204,
            "father_id": 192203,
            "users": [
                {
                    "uid": 11633,
                    "username": "bruce.zhang"
                }
            ]
        },
        {
            "name": "雪豹队",
            "is_hide": 1,
            "gid": 1743,
            "father_id": 1676,
            "users": []
        },
        {
            "name": "无锡市",
            "is_hide": 0,
            "gid": 192205,
            "father_id": 192203,
            "users": [
                {
                    "uid": 18026,
                    "username": "min.lv"
                }
            ]
        },
        {
            "name": "北京监理组",
            "is_hide": 1,
            "gid": 1744,
            "father_id": 1837,
            "users": []
        },
        {
            "name": "长沙市",
            "is_hide": 0,
            "gid": 192210,
            "father_id": 192203,
            "users": [
                {
                    "uid": 10893,
                    "username": "kane.qiu"
                }
            ]
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1745,
            "father_id": 1436,
            "users": [
                {
                    "uid": 1121,
                    "username": "jimmy.zhan"
                }
            ]
        },
        {
            "name": "上海市",
            "is_hide": 0,
            "gid": 192211,
            "father_id": 192203,
            "users": [
                {
                    "uid": 18168,
                    "username": "major.xu"
                }
            ]
        },
        {
            "name": "常州市",
            "is_hide": 0,
            "gid": 1746,
            "father_id": 2328,
            "users": [
                {
                    "uid": 17518,
                    "username": "hiyu.yu"
                },
                {
                    "uid": 1608,
                    "username": "rob.zhang"
                },
                {
                    "uid": 11083,
                    "username": "stephen.liu"
                },
                {
                    "uid": 11502,
                    "username": "smile.chu"
                },
                {
                    "uid": 12385,
                    "username": "carey.wu"
                }
            ]
        },
        {
            "name": "合肥市",
            "is_hide": 0,
            "gid": 192208,
            "father_id": 192203,
            "users": [
                {
                    "uid": 18006,
                    "username": "yao.xu"
                }
            ]
        },
        {
            "name": "成都市",
            "is_hide": 0,
            "gid": 1747,
            "father_id": 1829,
            "users": [
                {
                    "uid": 1366,
                    "username": "roy.li"
                },
                {
                    "uid": 739895,
                    "username": "viking.huang"
                },
                {
                    "uid": 10536,
                    "username": "allen.cha"
                },
                {
                    "uid": 92707,
                    "username": "bruce.xiao"
                },
                {
                    "uid": 11364,
                    "username": "darnell.tang"
                },
                {
                    "uid": 12476,
                    "username": "aurora.gong"
                },
                {
                    "uid": 12590,
                    "username": "shrek.hu"
                },
                {
                    "uid": 14513,
                    "username": "cristiano.jin"
                },
                {
                    "uid": 14838,
                    "username": "eric.su"
                },
                {
                    "uid": 15709,
                    "username": "burt.meng"
                },
                {
                    "uid": 15998,
                    "username": "collin.chen"
                },
                {
                    "uid": 16034,
                    "username": "tmac.wu"
                }
            ]
        },
        {
            "name": "武汉市",
            "is_hide": 0,
            "gid": 192209,
            "father_id": 192203,
            "users": [
                {
                    "uid": 1124,
                    "username": "rod.xiong"
                }
            ]
        },
        {
            "name": "广州市",
            "is_hide": 0,
            "gid": 1748,
            "father_id": 1834,
            "users": [
                {
                    "uid": 16641,
                    "username": "joke.fang"
                },
                {
                    "uid": 17792,
                    "username": "zongdi.zhang"
                },
                {
                    "uid": 1432,
                    "username": "jims.wu"
                },
                {
                    "uid": 83779,
                    "username": "jianming.zhang"
                },
                {
                    "uid": 10613,
                    "username": "simon.yin"
                },
                {
                    "uid": 10861,
                    "username": "bowen.zheng"
                },
                {
                    "uid": 11113,
                    "username": "ezreal.chen"
                },
                {
                    "uid": 11191,
                    "username": "duke.li"
                },
                {
                    "uid": 11348,
                    "username": "fighting.peng"
                },
                {
                    "uid": 12544,
                    "username": "bin.guo"
                },
                {
                    "uid": 14127,
                    "username": "sokey.shen"
                },
                {
                    "uid": 14278,
                    "username": "hugo.huang"
                },
                {
                    "uid": 14306,
                    "username": "albert.qiu"
                },
                {
                    "uid": 15697,
                    "username": "fawn.li"
                }
            ]
        },
        {
            "name": "贵阳市",
            "is_hide": 0,
            "gid": 1749,
            "father_id": 2333,
            "users": [
                {
                    "uid": 11275,
                    "username": "bob.yuan"
                },
                {
                    "uid": 734873,
                    "username": "liangkun.peng"
                },
                {
                    "uid": 15659,
                    "username": "yozo.mao"
                }
            ]
        },
        {
            "name": "郑州市",
            "is_hide": 0,
            "gid": 1750,
            "father_id": 2336,
            "users": [
                {
                    "uid": 10870,
                    "username": "truman.zhou"
                },
                {
                    "uid": 11481,
                    "username": "vencien.duan"
                },
                {
                    "uid": 11509,
                    "username": "roger.zhai"
                },
                {
                    "uid": 11801,
                    "username": "alan.jin"
                },
                {
                    "uid": 12396,
                    "username": "jackie.liu"
                }
            ]
        },
        {
            "name": "大连市",
            "is_hide": 0,
            "gid": 1751,
            "father_id": 2326,
            "users": [
                {
                    "uid": 89558,
                    "username": "barret.zhang"
                },
                {
                    "uid": 11244,
                    "username": "kosma.wang"
                },
                {
                    "uid": 11623,
                    "username": "martin.shi"
                },
                {
                    "uid": 11833,
                    "username": "alan.shi"
                },
                {
                    "uid": 15213,
                    "username": "winter.zhang"
                }
            ]
        },
        {
            "name": "苏州市",
            "is_hide": 0,
            "gid": 1753,
            "father_id": 2325,
            "users": [
                {
                    "uid": 17485,
                    "username": "zhaopeng.li"
                },
                {
                    "uid": 1417,
                    "username": "rove.liu"
                },
                {
                    "uid": 18277,
                    "username": "yafei.ding"
                },
                {
                    "uid": 92027,
                    "username": "jun.dai"
                },
                {
                    "uid": 14872,
                    "username": "jenkin.zhu"
                },
                {
                    "uid": 15130,
                    "username": "eugene.yang"
                }
            ]
        },
        {
            "name": "西安市",
            "is_hide": 0,
            "gid": 1755,
            "father_id": 1840,
            "users": [
                {
                    "uid": 17222,
                    "username": "cruze.dang"
                },
                {
                    "uid": 12504,
                    "username": "stafen.qin"
                },
                {
                    "uid": 12602,
                    "username": "albert.guo"
                },
                {
                    "uid": 12603,
                    "username": "aaron.hao"
                },
                {
                    "uid": 12604,
                    "username": "ethan.jiao"
                },
                {
                    "uid": 95490,
                    "username": "bobo.cui"
                },
                {
                    "uid": 30259,
                    "username": "tow.wang"
                }
            ]
        },
        {
            "name": "昆明市",
            "is_hide": 0,
            "gid": 1756,
            "father_id": 2333,
            "users": [
                {
                    "uid": 17742,
                    "username": "crazy.yang"
                },
                {
                    "uid": 11409,
                    "username": "allen.huang"
                },
                {
                    "uid": 14469,
                    "username": "libin.li"
                },
                {
                    "uid": 14550,
                    "username": "yuxiang.ma"
                },
                {
                    "uid": 14554,
                    "username": "loongc.xu"
                },
                {
                    "uid": 15562,
                    "username": "jasen.xu"
                }
            ]
        },
        {
            "name": "交互设计组",
            "is_hide": 0,
            "gid": 192222,
            "father_id": 1657,
            "users": [
                {
                    "uid": 745421,
                    "username": "ivy.yang"
                },
                {
                    "uid": 745410,
                    "username": "yoko.zeng"
                }
            ]
        },
        {
            "name": "用户体验研究组",
            "is_hide": 0,
            "gid": 192223,
            "father_id": 1657,
            "users": []
        },
        {
            "name": "南京市",
            "is_hide": 0,
            "gid": 1758,
            "father_id": 1836,
            "users": [
                {
                    "uid": 16908,
                    "username": "jason.qu"
                },
                {
                    "uid": 17209,
                    "username": "lan.mi"
                },
                {
                    "uid": 18093,
                    "username": "william.zhang"
                },
                {
                    "uid": 1913,
                    "username": "hilary.chen"
                },
                {
                    "uid": 11081,
                    "username": "berg.guo"
                },
                {
                    "uid": 11085,
                    "username": "lris.lai"
                },
                {
                    "uid": 11087,
                    "username": "neil.wang"
                },
                {
                    "uid": 11293,
                    "username": "elvis.tang"
                },
                {
                    "uid": 11294,
                    "username": "abel.zhu"
                },
                {
                    "uid": 11806,
                    "username": "baron.liu"
                },
                {
                    "uid": 12471,
                    "username": "ryan.song"
                },
                {
                    "uid": 14240,
                    "username": "darker.zhang"
                }
            ]
        },
        {
            "name": "天津市",
            "is_hide": 0,
            "gid": 1760,
            "father_id": 2327,
            "users": [
                {
                    "uid": 86371,
                    "username": "holy.deng"
                },
                {
                    "uid": 87145,
                    "username": "cheng.wang"
                },
                {
                    "uid": 92041,
                    "username": "ran.he"
                },
                {
                    "uid": 11107,
                    "username": "david.ma"
                },
                {
                    "uid": 11403,
                    "username": "baron.zhu"
                },
                {
                    "uid": 12406,
                    "username": "brandon.yu"
                },
                {
                    "uid": 14092,
                    "username": "wind.tian"
                }
            ]
        },
        {
            "name": "武汉市",
            "is_hide": 0,
            "gid": 1761,
            "father_id": 2337,
            "users": [
                {
                    "uid": 16743,
                    "username": "jk.yang"
                },
                {
                    "uid": 16745,
                    "username": "mible.hu"
                },
                {
                    "uid": 16752,
                    "username": "key.yang"
                },
                {
                    "uid": 17406,
                    "username": "tomas.xiong"
                },
                {
                    "uid": 17561,
                    "username": "jeff.yu"
                },
                {
                    "uid": 17827,
                    "username": "kevin.zhou"
                },
                {
                    "uid": 10108,
                    "username": "farmer.wang"
                },
                {
                    "uid": 12215,
                    "username": "bear.xiong"
                },
                {
                    "uid": 14177,
                    "username": "simple.zhao"
                },
                {
                    "uid": 14206,
                    "username": "bruce.wu"
                }
            ]
        },
        {
            "name": "线上推广部",
            "is_hide": 0,
            "gid": 192227,
            "father_id": 195825,
            "users": [
                {
                    "uid": 16270,
                    "username": "mellon.zhang"
                }
            ]
        },
        {
            "name": "南宁市",
            "is_hide": 0,
            "gid": 1762,
            "father_id": 2332,
            "users": [
                {
                    "uid": 1476,
                    "username": "winter.huang"
                },
                {
                    "uid": 11750,
                    "username": "owen.liang"
                },
                {
                    "uid": 14932,
                    "username": "aaron.xie"
                },
                {
                    "uid": 16205,
                    "username": "windy.wen"
                }
            ]
        },
        {
            "name": "装企产品部",
            "is_hide": 0,
            "gid": 192224,
            "father_id": 1366,
            "users": [
                {
                    "uid": 16597,
                    "username": "frank.liu"
                },
                {
                    "uid": 1847,
                    "username": "leo.duan"
                },
                {
                    "uid": 747003,
                    "username": "saida.xie"
                },
                {
                    "uid": 75995,
                    "username": "shawn.huang"
                },
                {
                    "uid": 10937,
                    "username": "grace.zhong"
                },
                {
                    "uid": 11440,
                    "username": "zed.zeng"
                },
                {
                    "uid": 30191,
                    "username": "share.yu"
                }
            ]
        },
        {
            "name": "上海1市",
            "is_hide": 0,
            "gid": 1763,
            "father_id": 2323,
            "users": [
                {
                    "uid": 16893,
                    "username": "rex.azhong"
                },
                {
                    "uid": 10441,
                    "username": "dave.wang"
                },
                {
                    "uid": 10705,
                    "username": "arven.zhang"
                },
                {
                    "uid": 11185,
                    "username": "peter.huang"
                },
                {
                    "uid": 11242,
                    "username": "bolang.yu"
                },
                {
                    "uid": 12345,
                    "username": "endy.wang"
                },
                {
                    "uid": 95750,
                    "username": "justine.wang"
                },
                {
                    "uid": 14523,
                    "username": "dana.luo"
                },
                {
                    "uid": 15135,
                    "username": "biyy.li"
                }
            ]
        },
        {
            "name": "设计师产品部",
            "is_hide": 0,
            "gid": 192225,
            "father_id": 1366,
            "users": [
                {
                    "uid": 65857,
                    "username": "wendy.guo"
                },
                {
                    "uid": 18348,
                    "username": "shirley.chang"
                },
                {
                    "uid": 56654,
                    "username": "will.tang"
                },
                {
                    "uid": 10543,
                    "username": "koko.wu"
                },
                {
                    "uid": 13852,
                    "username": "rex.wu"
                }
            ]
        },
        {
            "name": "长沙市",
            "is_hide": 0,
            "gid": 1765,
            "father_id": 2334,
            "users": [
                {
                    "uid": 10442,
                    "username": "jerry.xiao"
                },
                {
                    "uid": 10535,
                    "username": "mike.wu"
                },
                {
                    "uid": 10769,
                    "username": "roger.chen"
                },
                {
                    "uid": 10891,
                    "username": "tony.luo"
                },
                {
                    "uid": 11010,
                    "username": "jack.zhu"
                }
            ]
        },
        {
            "name": "合肥市",
            "is_hide": 0,
            "gid": 1767,
            "father_id": 2329,
            "users": [
                {
                    "uid": 10954,
                    "username": "dean.zhao"
                },
                {
                    "uid": 12009,
                    "username": "alvin.gao"
                },
                {
                    "uid": 12226,
                    "username": "sai.luo"
                },
                {
                    "uid": 30104,
                    "username": "zhiheng.qian"
                },
                {
                    "uid": 13839,
                    "username": "bart.zhao"
                }
            ]
        },
        {
            "name": "福州市",
            "is_hide": 0,
            "gid": 1768,
            "father_id": 2324,
            "users": [
                {
                    "uid": 11136,
                    "username": "yahyh.hu"
                }
            ]
        },
        {
            "name": "佛山市",
            "is_hide": 0,
            "gid": 1769,
            "father_id": 1834,
            "users": [
                {
                    "uid": 16714,
                    "username": "noodle.he"
                },
                {
                    "uid": 30266,
                    "username": "sam.pan"
                },
                {
                    "uid": 14928,
                    "username": "andy.mo"
                },
                {
                    "uid": 15005,
                    "username": "kokim.wu"
                }
            ]
        },
        {
            "name": "深圳市",
            "is_hide": 0,
            "gid": 1770,
            "father_id": 1834,
            "users": [
                {
                    "uid": 1266,
                    "username": "tab.li"
                },
                {
                    "uid": 1399,
                    "username": "leon.an"
                },
                {
                    "uid": 1464,
                    "username": "stephone.li"
                },
                {
                    "uid": 17860,
                    "username": "antony.zhou"
                },
                {
                    "uid": 1480,
                    "username": "alex.shi"
                },
                {
                    "uid": 1660,
                    "username": "garen.peng"
                },
                {
                    "uid": 10407,
                    "username": "shutao.li"
                },
                {
                    "uid": 10416,
                    "username": "angus.zhang"
                },
                {
                    "uid": 11140,
                    "username": "jerry.tan"
                },
                {
                    "uid": 11353,
                    "username": "blithe.xiao"
                },
                {
                    "uid": 11447,
                    "username": "carl.sun"
                },
                {
                    "uid": 14149,
                    "username": "gary.tan"
                },
                {
                    "uid": 14200,
                    "username": "antonio.li"
                },
                {
                    "uid": 14254,
                    "username": "lison.chen"
                }
            ]
        },
        {
            "name": "杭州市",
            "is_hide": 0,
            "gid": 1771,
            "father_id": 2322,
            "users": [
                {
                    "uid": 17887,
                    "username": "marcus.zhang"
                },
                {
                    "uid": 10532,
                    "username": "beck.li"
                },
                {
                    "uid": 10611,
                    "username": "happy.liu"
                },
                {
                    "uid": 12370,
                    "username": "nick.xi"
                },
                {
                    "uid": 94997,
                    "username": "tianxiang.xue"
                },
                {
                    "uid": 14172,
                    "username": "winner.li"
                },
                {
                    "uid": 16120,
                    "username": "maiy.mi"
                }
            ]
        },
        {
            "name": "沈阳市",
            "is_hide": 0,
            "gid": 1772,
            "father_id": 1837,
            "users": [
                {
                    "uid": 11598,
                    "username": "munin.han"
                },
                {
                    "uid": 11599,
                    "username": "cash.dai"
                },
                {
                    "uid": 11600,
                    "username": "john.li"
                },
                {
                    "uid": 12194,
                    "username": "number.du"
                },
                {
                    "uid": 12401,
                    "username": "firing.li"
                }
            ]
        },
        {
            "name": "昆山市",
            "is_hide": 0,
            "gid": 1773,
            "father_id": 2323,
            "users": [
                {
                    "uid": 16678,
                    "username": "max.yu"
                },
                {
                    "uid": 17791,
                    "username": "currzy.zhang"
                },
                {
                    "uid": 11141,
                    "username": "chuch.fan"
                }
            ]
        },
        {
            "name": "无锡市",
            "is_hide": 0,
            "gid": 1774,
            "father_id": 1836,
            "users": [
                {
                    "uid": 17420,
                    "username": "rong.zhu"
                },
                {
                    "uid": 17629,
                    "username": "sam.xie"
                },
                {
                    "uid": 18027,
                    "username": "weiwei.zhang"
                },
                {
                    "uid": 11273,
                    "username": "lan.zhou"
                },
                {
                    "uid": 12442,
                    "username": "alun.gao"
                },
                {
                    "uid": 12523,
                    "username": "jesson.luo"
                },
                {
                    "uid": 14251,
                    "username": "luson.yuan"
                }
            ]
        },
        {
            "name": "东莞市",
            "is_hide": 0,
            "gid": 1775,
            "father_id": 2331,
            "users": [
                {
                    "uid": 16825,
                    "username": "joey.wang"
                },
                {
                    "uid": 1882,
                    "username": "stellar.lu"
                },
                {
                    "uid": 2028,
                    "username": "tree.zhao"
                },
                {
                    "uid": 743861,
                    "username": "fei.chen"
                },
                {
                    "uid": 11992,
                    "username": "bevis.meng"
                }
            ]
        },
        {
            "name": "重庆市",
            "is_hide": 0,
            "gid": 1776,
            "father_id": 2335,
            "users": [
                {
                    "uid": 16712,
                    "username": "aian.liu"
                },
                {
                    "uid": 741248,
                    "username": "flying.zhang"
                },
                {
                    "uid": 92026,
                    "username": "nick.du"
                },
                {
                    "uid": 95040,
                    "username": "shy.zhang"
                },
                {
                    "uid": 14175,
                    "username": "caesar.dong"
                }
            ]
        },
        {
            "name": "厦门市",
            "is_hide": 0,
            "gid": 1777,
            "father_id": 2324,
            "users": [
                {
                    "uid": 10446,
                    "username": "kid.lin"
                },
                {
                    "uid": 10447,
                    "username": "wilson.zhong"
                },
                {
                    "uid": 12492,
                    "username": "alvin.guan"
                },
                {
                    "uid": 12583,
                    "username": "simon.chen"
                }
            ]
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1778,
            "father_id": 1284,
            "users": [
                {
                    "uid": 10869,
                    "username": "jinhui.qi"
                }
            ]
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1779,
            "father_id": 1285,
            "users": []
        },
        {
            "name": "交付二部",
            "is_hide": 0,
            "gid": 1780,
            "father_id": 1285,
            "users": []
        },
        {
            "name": "交付二部",
            "is_hide": 0,
            "gid": 1781,
            "father_id": 1310,
            "users": []
        },
        {
            "name": "交付二部",
            "is_hide": 0,
            "gid": 1784,
            "father_id": 1323,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1785,
            "father_id": 1323,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1786,
            "father_id": 1387,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1787,
            "father_id": 1321,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1788,
            "father_id": 1321,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1789,
            "father_id": 1283,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1790,
            "father_id": 1534,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1791,
            "father_id": 1386,
            "users": []
        },
        {
            "name": "交付二部",
            "is_hide": 0,
            "gid": 1792,
            "father_id": 1384,
            "users": [
                {
                    "uid": 17218,
                    "username": "jay.xiao"
                },
                {
                    "uid": 17354,
                    "username": "kitolai.li"
                },
                {
                    "uid": 17696,
                    "username": "liji.jiang"
                },
                {
                    "uid": 1414,
                    "username": "even.sheng"
                }
            ]
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1793,
            "father_id": 1384,
            "users": [
                {
                    "uid": 17990,
                    "username": "bonny.xu"
                },
                {
                    "uid": 18195,
                    "username": "yufeng.liu"
                },
                {
                    "uid": 30285,
                    "username": "hang.yang"
                },
                {
                    "uid": 16298,
                    "username": "tany.luo"
                }
            ]
        },
        {
            "name": "交付二部",
            "is_hide": 0,
            "gid": 1794,
            "father_id": 1295,
            "users": []
        },
        {
            "name": "交付三部",
            "is_hide": 0,
            "gid": 1795,
            "father_id": 1295,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1797,
            "father_id": 1295,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1798,
            "father_id": 1309,
            "users": []
        },
        {
            "name": "交付二部",
            "is_hide": 0,
            "gid": 1799,
            "father_id": 1309,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1800,
            "father_id": 1297,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1801,
            "father_id": 1342,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1802,
            "father_id": 1340,
            "users": [
                {
                    "uid": 12356,
                    "username": "boyce.li"
                }
            ]
        },
        {
            "name": "交付二部",
            "is_hide": 0,
            "gid": 1803,
            "father_id": 1340,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1804,
            "father_id": 1388,
            "users": []
        },
        {
            "name": "交付二部",
            "is_hide": 1,
            "gid": 1805,
            "father_id": 1926,
            "users": []
        },
        {
            "name": "交付三部",
            "is_hide": 1,
            "gid": 1806,
            "father_id": 1926,
            "users": []
        },
        {
            "name": "交付四部",
            "is_hide": 1,
            "gid": 1807,
            "father_id": 1926,
            "users": []
        },
        {
            "name": "财务管理部",
            "is_hide": 1,
            "gid": 1809,
            "father_id": 26,
            "users": []
        },
        {
            "name": "装修流程产品部",
            "is_hide": 0,
            "gid": 1810,
            "father_id": 1366,
            "users": [
                {
                    "uid": 18370,
                    "username": "sally.guo"
                },
                {
                    "uid": 13534,
                    "username": "lucy.wei"
                },
                {
                    "uid": 30024,
                    "username": "kobe.wang"
                },
                {
                    "uid": 30164,
                    "username": "stan.zhang"
                },
                {
                    "uid": 14671,
                    "username": "rita.liu"
                },
                {
                    "uid": 16306,
                    "username": "ellen.chen"
                }
            ]
        },
        {
            "name": "西安市场部",
            "is_hide": 0,
            "gid": 1811,
            "father_id": 1580,
            "users": []
        },
        {
            "name": "SQE部",
            "is_hide": 0,
            "gid": 1812,
            "father_id": 1120,
            "users": [
                {
                    "uid": 18237,
                    "username": "harry.zhu"
                }
            ]
        },
        {
            "name": "ERP数据管理部",
            "is_hide": 0,
            "gid": 1813,
            "father_id": 1120,
            "users": [
                {
                    "uid": 14683,
                    "username": "adrain.he"
                }
            ]
        },
        {
            "name": "咨询客服部",
            "is_hide": 0,
            "gid": 1815,
            "father_id": 2231,
            "users": [
                {
                    "uid": 84,
                    "username": "berry.li"
                },
                {
                    "uid": 1811,
                    "username": "anne.ma"
                }
            ]
        },
        {
            "name": "图满意约前管家",
            "is_hide": 1,
            "gid": 1816,
            "father_id": 1352,
            "users": []
        },
        {
            "name": "售后质检组",
            "is_hide": 1,
            "gid": 1817,
            "father_id": 1119,
            "users": []
        },
        {
            "name": "深圳财务组",
            "is_hide": 0,
            "gid": 1818,
            "father_id": 1721,
            "users": []
        },
        {
            "name": "广州财务组",
            "is_hide": 0,
            "gid": 1819,
            "father_id": 1721,
            "users": [
                {
                    "uid": 68325,
                    "username": "diana.du"
                },
                {
                    "uid": 16112,
                    "username": "leyna.lin"
                }
            ]
        },
        {
            "name": "北京财务组",
            "is_hide": 0,
            "gid": 1820,
            "father_id": 1721,
            "users": [
                {
                    "uid": 17957,
                    "username": "summy.zhang"
                },
                {
                    "uid": 17980,
                    "username": "silvia.guan"
                }
            ]
        },
        {
            "name": "上海财务组",
            "is_hide": 0,
            "gid": 1821,
            "father_id": 1721,
            "users": [
                {
                    "uid": 17083,
                    "username": "amily.peng"
                }
            ]
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1824,
            "father_id": 1296,
            "users": []
        },
        {
            "name": "交付三部",
            "is_hide": 1,
            "gid": 1825,
            "father_id": 1384,
            "users": []
        },
        {
            "name": "交付二部",
            "is_hide": 0,
            "gid": 1827,
            "father_id": 1322,
            "users": []
        },
        {
            "name": "综合支持部",
            "is_hide": 0,
            "gid": 1828,
            "father_id": 1722,
            "users": [
                {
                    "uid": 14923,
                    "username": "anne.xiao"
                }
            ]
        },
        {
            "name": "中西区",
            "is_hide": 0,
            "gid": 1829,
            "father_id": 1722,
            "users": [
                {
                    "uid": 734335,
                    "username": "zongquan.liang"
                }
            ]
        },
        {
            "name": "华南区",
            "is_hide": 0,
            "gid": 1834,
            "father_id": 1722,
            "users": [
                {
                    "uid": 10616,
                    "username": "victor.li"
                }
            ]
        },
        {
            "name": "成都大区",
            "is_hide": 1,
            "gid": 1835,
            "father_id": 1722,
            "users": []
        },
        {
            "name": "华东区",
            "is_hide": 0,
            "gid": 1836,
            "father_id": 1722,
            "users": []
        },
        {
            "name": "华北区",
            "is_hide": 0,
            "gid": 1837,
            "father_id": 1722,
            "users": [
                {
                    "uid": 10699,
                    "username": "tina.cui"
                },
                {
                    "uid": 30158,
                    "username": "peter.sun"
                }
            ]
        },
        {
            "name": "华东区",
            "is_hide": 1,
            "gid": 1838,
            "father_id": 1722,
            "users": []
        },
        {
            "name": "中原区",
            "is_hide": 0,
            "gid": 1840,
            "father_id": 1722,
            "users": [
                {
                    "uid": 734808,
                    "username": "boy.zheng"
                }
            ]
        },
        {
            "name": "B检组",
            "is_hide": 1,
            "gid": 1841,
            "father_id": 1747,
            "users": []
        },
        {
            "name": "测试456(0)",
            "is_hide": 1,
            "gid": 1843,
            "father_id": 1089,
            "users": []
        },
        {
            "name": "行业研究组",
            "is_hide": 1,
            "gid": 1844,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "安装与拓展中心",
            "is_hide": 1,
            "gid": 1845,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "武汉市场组",
            "is_hide": 1,
            "gid": 1846,
            "father_id": 2118,
            "users": []
        },
        {
            "name": "新盘电销质检",
            "is_hide": 1,
            "gid": 1847,
            "father_id": 1119,
            "users": []
        },
        {
            "name": "测试",
            "is_hide": 1,
            "gid": 1848,
            "father_id": 0,
            "users": []
        },
        {
            "name": "运营中心",
            "is_hide": 1,
            "gid": 1849,
            "father_id": 0,
            "users": []
        },
        {
            "name": "展厅运营部",
            "is_hide": 0,
            "gid": 1850,
            "father_id": 1120,
            "users": []
        },
        {
            "name": "设计组",
            "is_hide": 1,
            "gid": 1851,
            "father_id": 1907,
            "users": []
        },
        {
            "name": "项目组",
            "is_hide": 1,
            "gid": 1852,
            "father_id": 1907,
            "users": []
        },
        {
            "name": "商城部",
            "is_hide": 1,
            "gid": 1853,
            "father_id": 865,
            "users": []
        },
        {
            "name": "HRBP",
            "is_hide": 1,
            "gid": 1854,
            "father_id": 865,
            "users": []
        },
        {
            "name": "采购部",
            "is_hide": 0,
            "gid": 1855,
            "father_id": 1120,
            "users": []
        },
        {
            "name": "辅材运营部",
            "is_hide": 0,
            "gid": 1856,
            "father_id": 1204,
            "users": [
                {
                    "uid": 10025,
                    "username": "mata.zeng"
                },
                {
                    "uid": 11112,
                    "username": "andrew.hu"
                },
                {
                    "uid": 30087,
                    "username": "richard.zhao"
                }
            ]
        },
        {
            "name": "天空组",
            "is_hide": 1,
            "gid": 1857,
            "father_id": 1361,
            "users": []
        },
        {
            "name": "数据反馈组",
            "is_hide": 1,
            "gid": 1858,
            "father_id": 1367,
            "users": []
        },
        {
            "name": "物流部",
            "is_hide": 1,
            "gid": 1859,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "副总裁办",
            "is_hide": 1,
            "gid": 1860,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1861,
            "father_id": 1284,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1862,
            "father_id": 1285,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1863,
            "father_id": 1296,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1864,
            "father_id": 1297,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 1,
            "gid": 1865,
            "father_id": 1297,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1866,
            "father_id": 1309,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1867,
            "father_id": 1310,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1868,
            "father_id": 1311,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1869,
            "father_id": 1319,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1870,
            "father_id": 1320,
            "users": []
        },
        {
            "name": "商务合作部",
            "is_hide": 0,
            "gid": 194380,
            "father_id": 67,
            "users": [
                {
                    "uid": 1141,
                    "username": "abby.chang"
                },
                {
                    "uid": 91522,
                    "username": "shirley.yang"
                },
                {
                    "uid": 10857,
                    "username": "michelle.zhu"
                },
                {
                    "uid": 77289,
                    "username": "una.xu"
                }
            ]
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1871,
            "father_id": 1322,
            "users": []
        },
        {
            "name": "装企运营中心",
            "is_hide": 0,
            "gid": 194381,
            "father_id": 0,
            "users": [
                {
                    "uid": 18,
                    "username": "joy.dong"
                },
                {
                    "uid": 65847,
                    "username": "david.duan"
                },
                {
                    "uid": 65848,
                    "username": "garrett.gong"
                },
                {
                    "uid": 65850,
                    "username": "harden.zhu"
                },
                {
                    "uid": 65853,
                    "username": "rocky.wang"
                },
                {
                    "uid": 65864,
                    "username": "meria.ma"
                },
                {
                    "uid": 65866,
                    "username": "richard.li"
                },
                {
                    "uid": 66032,
                    "username": "carole.huang"
                },
                {
                    "uid": 17006,
                    "username": "panw.luo"
                },
                {
                    "uid": 17423,
                    "username": "color.he"
                },
                {
                    "uid": 17436,
                    "username": "rio.yang"
                },
                {
                    "uid": 1298,
                    "username": "yaung.xie"
                },
                {
                    "uid": 1309,
                    "username": "una.zhao"
                },
                {
                    "uid": 17706,
                    "username": "antonio.zhang"
                },
                {
                    "uid": 17718,
                    "username": "grace.yu"
                },
                {
                    "uid": 1460,
                    "username": "melody.lin"
                },
                {
                    "uid": 1529,
                    "username": "fly.yan"
                },
                {
                    "uid": 1645,
                    "username": "leon.du"
                },
                {
                    "uid": 1651,
                    "username": "johnny.zhang"
                },
                {
                    "uid": 1661,
                    "username": "weike.deng"
                },
                {
                    "uid": 1694,
                    "username": "tony.chen"
                },
                {
                    "uid": 1710,
                    "username": "beardy.huang"
                },
                {
                    "uid": 1711,
                    "username": "rolings.luo"
                },
                {
                    "uid": 18143,
                    "username": "jacky.wu"
                },
                {
                    "uid": 1823,
                    "username": "wenjie.bai"
                },
                {
                    "uid": 18222,
                    "username": "dean.zhang"
                },
                {
                    "uid": 18233,
                    "username": "peral.gu"
                },
                {
                    "uid": 1953,
                    "username": "legos.ying"
                },
                {
                    "uid": 1960,
                    "username": "lan.wei"
                },
                {
                    "uid": 2012,
                    "username": "dave.dong"
                },
                {
                    "uid": 2041,
                    "username": "liqun.zhang"
                },
                {
                    "uid": 2064,
                    "username": "rocket.zhao"
                },
                {
                    "uid": 2101,
                    "username": "star.chen"
                },
                {
                    "uid": 2140,
                    "username": "scott.peng"
                },
                {
                    "uid": 67792,
                    "username": "steve.zhang"
                },
                {
                    "uid": 68017,
                    "username": "mora.chen"
                },
                {
                    "uid": 87150,
                    "username": "xun.li"
                },
                {
                    "uid": 743290,
                    "username": "randy.wei"
                },
                {
                    "uid": 88155,
                    "username": "jacky.zhang"
                },
                {
                    "uid": 88401,
                    "username": "parker.wen"
                },
                {
                    "uid": 56541,
                    "username": "andrew.zhou"
                },
                {
                    "uid": 91074,
                    "username": "mona.xu"
                },
                {
                    "uid": 10068,
                    "username": "easy.chen"
                },
                {
                    "uid": 10119,
                    "username": "karl.dong"
                },
                {
                    "uid": 10136,
                    "username": "brilliant.deng"
                },
                {
                    "uid": 10281,
                    "username": "jessy.bao"
                },
                {
                    "uid": 10428,
                    "username": "feel.xu"
                },
                {
                    "uid": 10429,
                    "username": "ben.wu"
                },
                {
                    "uid": 10549,
                    "username": "king.huang"
                },
                {
                    "uid": 10762,
                    "username": "aluin.li"
                },
                {
                    "uid": 10902,
                    "username": "angel.li"
                },
                {
                    "uid": 10939,
                    "username": "herman.li"
                },
                {
                    "uid": 10986,
                    "username": "tom.cao"
                },
                {
                    "uid": 10995,
                    "username": "derek.wang"
                },
                {
                    "uid": 11062,
                    "username": "adolph.wei"
                },
                {
                    "uid": 11076,
                    "username": "ykaitou.yang"
                },
                {
                    "uid": 11132,
                    "username": "alan.lv"
                },
                {
                    "uid": 11154,
                    "username": "curry.dan"
                },
                {
                    "uid": 11157,
                    "username": "peter.ding"
                },
                {
                    "uid": 11359,
                    "username": "vito.chen"
                },
                {
                    "uid": 11444,
                    "username": "evan.xia"
                },
                {
                    "uid": 11469,
                    "username": "jason.heng"
                },
                {
                    "uid": 11475,
                    "username": "mj.ye"
                },
                {
                    "uid": 11525,
                    "username": "yuwne.zou"
                },
                {
                    "uid": 11561,
                    "username": "duke.chen"
                },
                {
                    "uid": 11572,
                    "username": "ryan.deng"
                },
                {
                    "uid": 11998,
                    "username": "lucky.li"
                },
                {
                    "uid": 12049,
                    "username": "bob.jiang"
                },
                {
                    "uid": 12219,
                    "username": "shalron.shan"
                },
                {
                    "uid": 12404,
                    "username": "edison.yang"
                },
                {
                    "uid": 30128,
                    "username": "anson.li"
                },
                {
                    "uid": 30163,
                    "username": "joe.shi"
                },
                {
                    "uid": 30194,
                    "username": "judy.zhong"
                },
                {
                    "uid": 14289,
                    "username": "joylin.yin"
                },
                {
                    "uid": 14500,
                    "username": "zoey.hou"
                },
                {
                    "uid": 14766,
                    "username": "jarid.yu"
                },
                {
                    "uid": 14820,
                    "username": "dolly.yang"
                },
                {
                    "uid": 14908,
                    "username": "peri.wang"
                },
                {
                    "uid": 15155,
                    "username": "suki.liu"
                },
                {
                    "uid": 15646,
                    "username": "julie.zhao"
                },
                {
                    "uid": 15757,
                    "username": "bod.fu"
                },
                {
                    "uid": 16002,
                    "username": "lonny.li"
                },
                {
                    "uid": 737066,
                    "username": "bill.liu"
                },
                {
                    "uid": 16278,
                    "username": "pope.cheng"
                }
            ]
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1872,
            "father_id": 1339,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1873,
            "father_id": 1340,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1874,
            "father_id": 1341,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1875,
            "father_id": 1342,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1876,
            "father_id": 1385,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1877,
            "father_id": 1386,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1878,
            "father_id": 1387,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1879,
            "father_id": 1388,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1880,
            "father_id": 1425,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1881,
            "father_id": 1534,
            "users": []
        },
        {
            "name": "督导部",
            "is_hide": 1,
            "gid": 1882,
            "father_id": 1860,
            "users": []
        },
        {
            "name": "核算组",
            "is_hide": 1,
            "gid": 1883,
            "father_id": 1927,
            "users": []
        },
        {
            "name": "工模客服部",
            "is_hide": 1,
            "gid": 1884,
            "father_id": 2135,
            "users": []
        },
        {
            "name": "重庆市场部",
            "is_hide": 0,
            "gid": 1885,
            "father_id": 1650,
            "users": []
        },
        {
            "name": "沈阳市场部",
            "is_hide": 0,
            "gid": 1886,
            "father_id": 1574,
            "users": []
        },
        {
            "name": "合肥财务组",
            "is_hide": 0,
            "gid": 1887,
            "father_id": 1721,
            "users": []
        },
        {
            "name": "无锡市场部",
            "is_hide": 0,
            "gid": 1888,
            "father_id": 1571,
            "users": []
        },
        {
            "name": "南京财务组",
            "is_hide": 0,
            "gid": 1889,
            "father_id": 1721,
            "users": []
        },
        {
            "name": "武汉财务组",
            "is_hide": 0,
            "gid": 1890,
            "father_id": 1721,
            "users": []
        },
        {
            "name": "长沙财务组",
            "is_hide": 0,
            "gid": 1891,
            "father_id": 1721,
            "users": []
        },
        {
            "name": "无锡财务组",
            "is_hide": 0,
            "gid": 1892,
            "father_id": 1721,
            "users": []
        },
        {
            "name": "苏州财务组",
            "is_hide": 0,
            "gid": 1893,
            "father_id": 1721,
            "users": []
        },
        {
            "name": "东莞财务组",
            "is_hide": 0,
            "gid": 1894,
            "father_id": 1721,
            "users": []
        },
        {
            "name": "组织发展部",
            "is_hide": 0,
            "gid": 1895,
            "father_id": 3,
            "users": [
                {
                    "uid": 747494,
                    "username": "wu.zhang"
                },
                {
                    "uid": 30009,
                    "username": "travis.wang"
                },
                {
                    "uid": 15384,
                    "username": "iris.wang"
                },
                {
                    "uid": 15711,
                    "username": "terry.liu"
                }
            ]
        },
        {
            "name": "测试部",
            "is_hide": 0,
            "gid": 1896,
            "father_id": 583,
            "users": [
                {
                    "uid": 18207,
                    "username": "hongfeng.huang"
                }
            ]
        },
        {
            "name": "北京RDC",
            "is_hide": 0,
            "gid": 1897,
            "father_id": 1234,
            "users": []
        },
        {
            "name": "广州RDC",
            "is_hide": 0,
            "gid": 1898,
            "father_id": 1384,
            "users": [
                {
                    "uid": 17654,
                    "username": "meilin.yang"
                },
                {
                    "uid": 91721,
                    "username": "yingming.tu"
                },
                {
                    "uid": 11582,
                    "username": "wade.tu"
                }
            ]
        },
        {
            "name": "上海RDC",
            "is_hide": 0,
            "gid": 1899,
            "father_id": 1234,
            "users": []
        },
        {
            "name": "深圳RDC",
            "is_hide": 0,
            "gid": 1900,
            "father_id": 1926,
            "users": [
                {
                    "uid": 17901,
                    "username": "roy.chen"
                }
            ]
        },
        {
            "name": "霹雳队",
            "is_hide": 1,
            "gid": 1901,
            "father_id": 1816,
            "users": []
        },
        {
            "name": "订单预算组",
            "is_hide": 1,
            "gid": 1902,
            "father_id": 1907,
            "users": []
        },
        {
            "name": "深化组",
            "is_hide": 1,
            "gid": 1903,
            "father_id": 1907,
            "users": []
        },
        {
            "name": "佛山市场部",
            "is_hide": 0,
            "gid": 1904,
            "father_id": 1584,
            "users": []
        },
        {
            "name": "雄鹰队",
            "is_hide": 1,
            "gid": 1905,
            "father_id": 1676,
            "users": []
        },
        {
            "name": "产品运营组",
            "is_hide": 1,
            "gid": 1906,
            "father_id": 1015,
            "users": []
        },
        {
            "name": "门店拓展部",
            "is_hide": 1,
            "gid": 1907,
            "father_id": 1204,
            "users": []
        },
        {
            "name": "南昌交付部",
            "is_hide": 0,
            "gid": 1908,
            "father_id": 1912,
            "users": []
        },
        {
            "name": "综合部",
            "is_hide": 0,
            "gid": 1909,
            "father_id": 1908,
            "users": []
        },
        {
            "name": "交付一部",
            "is_hide": 0,
            "gid": 1910,
            "father_id": 1908,
            "users": []
        },
        {
            "name": "安装服务部",
            "is_hide": 0,
            "gid": 1911,
            "father_id": 1908,
            "users": []
        },
        {
            "name": "南昌分公司",
            "is_hide": 0,
            "gid": 1912,
            "father_id": 2200,
            "users": [
                {
                    "uid": 1462,
                    "username": "upward.li"
                }
            ]
        },
        {
            "name": "云设计师组",
            "is_hide": 0,
            "gid": 1913,
            "father_id": 1912,
            "users": []
        },
        {
            "name": "南昌市场部",
            "is_hide": 0,
            "gid": 1914,
            "father_id": 1912,
            "users": []
        },
        {
            "name": "深圳大区",
            "is_hide": 1,
            "gid": 1915,
            "father_id": 6,
            "users": []
        },
        {
            "name": "华东二区",
            "is_hide": 1,
            "gid": 1916,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "上海大区",
            "is_hide": 1,
            "gid": 1917,
            "father_id": 6,
            "users": []
        },
        {
            "name": "西南区",
            "is_hide": 1,
            "gid": 1918,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "长沙大区",
            "is_hide": 1,
            "gid": 1919,
            "father_id": 6,
            "users": []
        },
        {
            "name": "西北区",
            "is_hide": 1,
            "gid": 1920,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "南昌BP",
            "is_hide": 0,
            "gid": 1921,
            "father_id": 1945,
            "users": [
                {
                    "uid": 76095,
                    "username": "irene.zhang"
                }
            ]
        },
        {
            "name": "土巴兔（深圳）装饰设计工程有限公司",
            "is_hide": 0,
            "gid": 1922,
            "father_id": 0,
            "users": []
        },
        {
            "name": "北京大区",
            "is_hide": 1,
            "gid": 1923,
            "father_id": 6,
            "users": []
        },
        {
            "name": "华中区",
            "is_hide": 1,
            "gid": 1924,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "广州大区",
            "is_hide": 1,
            "gid": 1925,
            "father_id": 6,
            "users": []
        },
        {
            "name": "深圳交付部",
            "is_hide": 0,
            "gid": 1926,
            "father_id": 1582,
            "users": [
                {
                    "uid": 30004,
                    "username": "fei.yu"
                }
            ]
        },
        {
            "name": "交付认证部",
            "is_hide": 0,
            "gid": 1927,
            "father_id": 1204,
            "users": [
                {
                    "uid": 18456,
                    "username": "shiming.huang"
                }
            ]
        },
        {
            "name": "标准品采购-瓷砖",
            "is_hide": 0,
            "gid": 1928,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "标准品采购-地板",
            "is_hide": 0,
            "gid": 1929,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "标准品采购-吊顶",
            "is_hide": 0,
            "gid": 1930,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "标准品采购-卫浴",
            "is_hide": 0,
            "gid": 1931,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "辅材类采购-辅料",
            "is_hide": 0,
            "gid": 1932,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "订制品采购-木门",
            "is_hide": 0,
            "gid": 1933,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "订制品采购-铝门",
            "is_hide": 0,
            "gid": 1934,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "订制品采购-橱柜",
            "is_hide": 0,
            "gid": 1935,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "软装类采购-电器",
            "is_hide": 0,
            "gid": 1936,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "软装类采购-家具",
            "is_hide": 0,
            "gid": 1937,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "软装类采购-饰品",
            "is_hide": 0,
            "gid": 1938,
            "father_id": 1855,
            "users": []
        },
        {
            "name": "审计部",
            "is_hide": 0,
            "gid": 1939,
            "father_id": 0,
            "users": [
                {
                    "uid": 1091,
                    "username": "abner.huang"
                },
                {
                    "uid": 743291,
                    "username": "brian.zhu"
                },
                {
                    "uid": 78319,
                    "username": "kris.li"
                },
                {
                    "uid": 30042,
                    "username": "kevin.mi"
                },
                {
                    "uid": 30043,
                    "username": "jackey.chen"
                },
                {
                    "uid": 15346,
                    "username": "jack.liang"
                }
            ]
        },
        {
            "name": "南昌市",
            "is_hide": 0,
            "gid": 1940,
            "father_id": 2322,
            "users": [
                {
                    "uid": 11189,
                    "username": "marvin.yi"
                },
                {
                    "uid": 30080,
                    "username": "bard.song"
                }
            ]
        },
        {
            "name": "南昌运营组",
            "is_hide": 0,
            "gid": 1941,
            "father_id": 1912,
            "users": [
                {
                    "uid": 91075,
                    "username": "ian.guang"
                },
                {
                    "uid": 92750,
                    "username": "allen.qu"
                }
            ]
        },
        {
            "name": "区域BP组",
            "is_hide": 1,
            "gid": 1942,
            "father_id": 1129,
            "users": []
        },
        {
            "name": "事业部BP组",
            "is_hide": 0,
            "gid": 1943,
            "father_id": 1129,
            "users": [
                {
                    "uid": 34,
                    "username": "carrie.huang"
                },
                {
                    "uid": 16917,
                    "username": "cherry.cui"
                },
                {
                    "uid": 1497,
                    "username": "echo.hu"
                },
                {
                    "uid": 76747,
                    "username": "xiaoling.deng"
                },
                {
                    "uid": 15437,
                    "username": "eva.yang"
                },
                {
                    "uid": 16286,
                    "username": "jerry.jiu"
                }
            ]
        },
        {
            "name": "华东区域BP组",
            "is_hide": 0,
            "gid": 1944,
            "father_id": 1129,
            "users": [
                {
                    "uid": 15868,
                    "username": "fan.yang"
                }
            ]
        },
        {
            "name": "东南区域BP组",
            "is_hide": 0,
            "gid": 1945,
            "father_id": 1129,
            "users": [
                {
                    "uid": 18445,
                    "username": "nicol.zeng"
                }
            ]
        },
        {
            "name": "华北区域BP组",
            "is_hide": 0,
            "gid": 1946,
            "father_id": 1129,
            "users": [
                {
                    "uid": 16821,
                    "username": "emily.shi"
                }
            ]
        },
        {
            "name": "中西区域BP组",
            "is_hide": 0,
            "gid": 1947,
            "father_id": 1129,
            "users": []
        },
        {
            "name": "武汉RDC",
            "is_hide": 0,
            "gid": 1948,
            "father_id": 1234,
            "users": []
        },
        {
            "name": "东莞DC",
            "is_hide": 1,
            "gid": 1949,
            "father_id": 1898,
            "users": []
        },
        {
            "name": "佛山DC",
            "is_hide": 1,
            "gid": 1950,
            "father_id": 1898,
            "users": []
        },
        {
            "name": "福州DC",
            "is_hide": 1,
            "gid": 1951,
            "father_id": 1898,
            "users": []
        },
        {
            "name": "厦门DC",
            "is_hide": 1,
            "gid": 1952,
            "father_id": 1898,
            "users": []
        },
        {
            "name": "南宁DC",
            "is_hide": 1,
            "gid": 1953,
            "father_id": 1898,
            "users": []
        },
        {
            "name": "南京DC",
            "is_hide": 1,
            "gid": 1954,
            "father_id": 1899,
            "users": []
        },
        {
            "name": "合肥DC",
            "is_hide": 1,
            "gid": 1955,
            "father_id": 1899,
            "users": []
        },
        {
            "name": "常州DC",
            "is_hide": 1,
            "gid": 1956,
            "father_id": 1899,
            "users": []
        },
        {
            "name": "苏州DC",
            "is_hide": 1,
            "gid": 1957,
            "father_id": 1899,
            "users": []
        },
        {
            "name": "无锡DC",
            "is_hide": 0,
            "gid": 1958,
            "father_id": 1899,
            "users": []
        },
        {
            "name": "昆山DC",
            "is_hide": 1,
            "gid": 1959,
            "father_id": 1899,
            "users": []
        },
        {
            "name": "杭州DC",
            "is_hide": 1,
            "gid": 1960,
            "father_id": 1899,
            "users": []
        },
        {
            "name": "天津DC",
            "is_hide": 1,
            "gid": 1961,
            "father_id": 1897,
            "users": []
        },
        {
            "name": "沈阳DC",
            "is_hide": 1,
            "gid": 1962,
            "father_id": 1897,
            "users": []
        },
        {
            "name": "大连DC",
            "is_hide": 1,
            "gid": 1963,
            "father_id": 1897,
            "users": []
        },
        {
            "name": "长沙DC",
            "is_hide": 1,
            "gid": 1964,
            "father_id": 1948,
            "users": []
        },
        {
            "name": "南昌DC",
            "is_hide": 1,
            "gid": 1965,
            "father_id": 1948,
            "users": []
        },
        {
            "name": "郑州DC",
            "is_hide": 1,
            "gid": 1966,
            "father_id": 1948,
            "users": []
        },
        {
            "name": "成都RDC",
            "is_hide": 1,
            "gid": 1967,
            "father_id": 1234,
            "users": []
        },
        {
            "name": "重庆DC",
            "is_hide": 1,
            "gid": 1968,
            "father_id": 1967,
            "users": []
        },
        {
            "name": "贵阳DC",
            "is_hide": 1,
            "gid": 1969,
            "father_id": 1967,
            "users": []
        },
        {
            "name": "昆明DC",
            "is_hide": 1,
            "gid": 1970,
            "father_id": 1967,
            "users": []
        },
        {
            "name": "西安DC",
            "is_hide": 1,
            "gid": 1971,
            "father_id": 1967,
            "users": []
        },
        {
            "name": "昆明市场部",
            "is_hide": 0,
            "gid": 1972,
            "father_id": 1581,
            "users": []
        },
        {
            "name": "杭州市场部",
            "is_hide": 0,
            "gid": 1973,
            "father_id": 1579,
            "users": []
        },
        {
            "name": "贵阳市场部",
            "is_hide": 0,
            "gid": 1974,
            "father_id": 1587,
            "users": []
        },
        {
            "name": "交付部",
            "is_hide": 0,
            "gid": 1975,
            "father_id": 1927,
            "users": [
                {
                    "uid": 10533,
                    "username": "henry.yan"
                }
            ]
        },
        {
            "name": "常州市场部",
            "is_hide": 0,
            "gid": 1976,
            "father_id": 1570,
            "users": []
        },
        {
            "name": "昆山市场部",
            "is_hide": 0,
            "gid": 1977,
            "father_id": 1577,
            "users": []
        },
        {
            "name": "郑州市场部",
            "is_hide": 0,
            "gid": 1978,
            "father_id": 1567,
            "users": []
        },
        {
            "name": "天津市场部",
            "is_hide": 0,
            "gid": 1979,
            "father_id": 1578,
            "users": []
        },
        {
            "name": "北京DC",
            "is_hide": 0,
            "gid": 1980,
            "father_id": 1897,
            "users": []
        },
        {
            "name": "广州DC",
            "is_hide": 1,
            "gid": 1981,
            "father_id": 1898,
            "users": []
        },
        {
            "name": "上海DC",
            "is_hide": 1,
            "gid": 1982,
            "father_id": 1899,
            "users": []
        },
        {
            "name": "武汉DC",
            "is_hide": 0,
            "gid": 1983,
            "father_id": 1948,
            "users": []
        },
        {
            "name": "成都DC",
            "is_hide": 1,
            "gid": 1984,
            "father_id": 1967,
            "users": []
        },
        {
            "name": "业务支持部",
            "is_hide": 0,
            "gid": 1985,
            "father_id": 1204,
            "users": [
                {
                    "uid": 1998,
                    "username": "tony.miao"
                },
                {
                    "uid": 11543,
                    "username": "hailly.chen"
                }
            ]
        },
        {
            "name": "供应链项目组",
            "is_hide": 1,
            "gid": 1986,
            "father_id": 1120,
            "users": []
        },
        {
            "name": "区域运营中心",
            "is_hide": 1,
            "gid": 1987,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "线上拓展部",
            "is_hide": 0,
            "gid": 1988,
            "father_id": 1609,
            "users": [
                {
                    "uid": 741480,
                    "username": "mikeli.li"
                },
                {
                    "uid": 10822,
                    "username": "smary.zeng"
                }
            ]
        },
        {
            "name": "东莞大区",
            "is_hide": 1,
            "gid": 1989,
            "father_id": 6,
            "users": []
        },
        {
            "name": "华北二区",
            "is_hide": 1,
            "gid": 1990,
            "father_id": 1609,
            "users": []
        },
        {
            "name": "北京展厅运营组",
            "is_hide": 0,
            "gid": 1991,
            "father_id": 1575,
            "users": []
        },
        {
            "name": "南京展厅运营组",
            "is_hide": 0,
            "gid": 1992,
            "father_id": 1566,
            "users": []
        },
        {
            "name": "苏州展厅运营组",
            "is_hide": 0,
            "gid": 1993,
            "father_id": 1568,
            "users": []
        },
        {
            "name": "上海展厅运营组",
            "is_hide": 0,
            "gid": 1994,
            "father_id": 1576,
            "users": []
        },
        {
            "name": "广州展厅运营组",
            "is_hide": 1,
            "gid": 1995,
            "father_id": 1583,
            "users": []
        },
        {
            "name": "龙岗展厅运营组",
            "is_hide": 1,
            "gid": 1996,
            "father_id": 1850,
            "users": []
        },
        {
            "name": "南山展厅运营组",
            "is_hide": 1,
            "gid": 1997,
            "father_id": 1582,
            "users": []
        },
        {
            "name": "长沙展厅运营组",
            "is_hide": 1,
            "gid": 1998,
            "father_id": 1586,
            "users": []
        },
        {
            "name": "武汉展厅运营组",
            "is_hide": 0,
            "gid": 1999,
            "father_id": 1591,
            "users": []
        },
        {
            "name": "产品研究组",
            "is_hide": 1,
            "gid": 2000,
            "father_id": 907,
            "users": []
        },
        {
            "name": "市场产品支持组",
            "is_hide": 1,
            "gid": 2001,
            "father_id": 907,
            "users": []
        },
        {
            "name": "木作采购组",
            "is_hide": 0,
            "gid": 2002,
            "father_id": 1855,
            "users": [
                {
                    "uid": 1223,
                    "username": "tealin.li"
                },
                {
                    "uid": 11355,
                    "username": "rick.liu"
                }
            ]
        },
        {
            "name": "软装/智能采购组",
            "is_hide": 0,
            "gid": 2003,
            "father_id": 1855,
            "users": [
                {
                    "uid": 12253,
                    "username": "april.wang"
                },
                {
                    "uid": 15153,
                    "username": "tim.you"
                }
            ]
        },
        {
            "name": "主材采购组",
            "is_hide": 0,
            "gid": 2004,
            "father_id": 1855,
            "users": [
                {
                    "uid": 18001,
                    "username": "figo.lv"
                },
                {
                    "uid": 12512,
                    "username": "cassiel.xu"
                },
                {
                    "uid": 14583,
                    "username": "cosima.liu"
                }
            ]
        },
        {
            "name": "云工长平台事业部",
            "is_hide": 1,
            "gid": 2005,
            "father_id": 0,
            "users": []
        },
        {
            "name": "SEO技术组",
            "is_hide": 0,
            "gid": 2006,
            "father_id": 195825,
            "users": [
                {
                    "uid": 16705,
                    "username": "cindy.fan"
                },
                {
                    "uid": 1208,
                    "username": "ginson.wang"
                },
                {
                    "uid": 1772,
                    "username": "michale.wu"
                },
                {
                    "uid": 745579,
                    "username": "douglas.liu"
                }
            ]
        },
        {
            "name": "内容运营组",
            "is_hide": 0,
            "gid": 2007,
            "father_id": 2234,
            "users": [
                {
                    "uid": 1178,
                    "username": "kusi.tao"
                },
                {
                    "uid": 10552,
                    "username": "kelly.xu"
                },
                {
                    "uid": 10605,
                    "username": "janice.xiao"
                }
            ]
        },
        {
            "name": "400接听组",
            "is_hide": 0,
            "gid": 2008,
            "father_id": 1815,
            "users": [
                {
                    "uid": 16800,
                    "username": "vivi.chen"
                },
                {
                    "uid": 65969,
                    "username": "harvey.chen"
                },
                {
                    "uid": 17196,
                    "username": "dave.liang"
                },
                {
                    "uid": 17849,
                    "username": "queena.huang"
                },
                {
                    "uid": 67059,
                    "username": "mary.gao"
                },
                {
                    "uid": 17912,
                    "username": "cher.lei"
                },
                {
                    "uid": 17916,
                    "username": "grace.lu"
                },
                {
                    "uid": 17917,
                    "username": "tracy.pang"
                },
                {
                    "uid": 1550,
                    "username": "sugar.tang"
                },
                {
                    "uid": 1791,
                    "username": "michelle.huang"
                },
                {
                    "uid": 68880,
                    "username": "mei.zhang"
                },
                {
                    "uid": 14803,
                    "username": "kailyn.zhong"
                },
                {
                    "uid": 735952,
                    "username": "talent.wang"
                },
                {
                    "uid": 15953,
                    "username": "betty.zheng"
                }
            ]
        },
        {
            "name": "微信在线组",
            "is_hide": 0,
            "gid": 2009,
            "father_id": 1815,
            "users": [
                {
                    "uid": 17240,
                    "username": "aimee.chen"
                },
                {
                    "uid": 17443,
                    "username": "tilan.li"
                },
                {
                    "uid": 18411,
                    "username": "lemon.yang"
                },
                {
                    "uid": 30261,
                    "username": "lin.meng"
                },
                {
                    "uid": 96832,
                    "username": "icey.ai"
                },
                {
                    "uid": 14960,
                    "username": "kally.xu"
                },
                {
                    "uid": 16043,
                    "username": "cookie.zhu"
                }
            ]
        },
        {
            "name": "客服质检部",
            "is_hide": 0,
            "gid": 2010,
            "father_id": 2231,
            "users": [
                {
                    "uid": 1605,
                    "username": "carol.tan"
                },
                {
                    "uid": 1869,
                    "username": "jerry.wu"
                },
                {
                    "uid": 1899,
                    "username": "joyce.long"
                },
                {
                    "uid": 10217,
                    "username": "maria.ye"
                },
                {
                    "uid": 10256,
                    "username": "bill.chen"
                },
                {
                    "uid": 10318,
                    "username": "lily.gu"
                },
                {
                    "uid": 10351,
                    "username": "cherry.gong"
                },
                {
                    "uid": 10354,
                    "username": "arron.yang"
                },
                {
                    "uid": 10524,
                    "username": "michelle.tang"
                },
                {
                    "uid": 11202,
                    "username": "nancy.liang"
                },
                {
                    "uid": 11663,
                    "username": "lynn.li"
                },
                {
                    "uid": 11671,
                    "username": "yoyo.liu"
                },
                {
                    "uid": 12021,
                    "username": "sophie.yu"
                },
                {
                    "uid": 12314,
                    "username": "sofia.qiu"
                },
                {
                    "uid": 15888,
                    "username": "snail.yang"
                },
                {
                    "uid": 16044,
                    "username": "ava.yang"
                },
                {
                    "uid": 16059,
                    "username": "riya.wang"
                }
            ]
        },
        {
            "name": "北一组",
            "is_hide": 0,
            "gid": 2011,
            "father_id": 2261,
            "users": [
                {
                    "uid": 16998,
                    "username": "beckham.xu"
                },
                {
                    "uid": 56554,
                    "username": "minjiang.cai"
                },
                {
                    "uid": 56621,
                    "username": "annie.he"
                },
                {
                    "uid": 10044,
                    "username": "luosi.luo"
                },
                {
                    "uid": 10160,
                    "username": "zoe.he"
                },
                {
                    "uid": 11421,
                    "username": "wing.ye"
                },
                {
                    "uid": 14625,
                    "username": "ellen.liu"
                },
                {
                    "uid": 15247,
                    "username": "alice.zhao"
                },
                {
                    "uid": 16134,
                    "username": "anja.huang"
                }
            ]
        },
        {
            "name": "落地西南组",
            "is_hide": 1,
            "gid": 2012,
            "father_id": 1352,
            "users": []
        },
        {
            "name": "南二组",
            "is_hide": 0,
            "gid": 2013,
            "father_id": 2260,
            "users": [
                {
                    "uid": 737351,
                    "username": "minyong.tang"
                },
                {
                    "uid": 737606,
                    "username": "arlin.xu"
                },
                {
                    "uid": 17145,
                    "username": "guifeng.huang"
                },
                {
                    "uid": 18229,
                    "username": "znna.liu"
                },
                {
                    "uid": 2009,
                    "username": "sunny.ouyang"
                },
                {
                    "uid": 56522,
                    "username": "yanmeng.li"
                },
                {
                    "uid": 11064,
                    "username": "yuki.wu"
                },
                {
                    "uid": 11424,
                    "username": "winni.liu"
                },
                {
                    "uid": 30232,
                    "username": "sophia.shen"
                },
                {
                    "uid": 15791,
                    "username": "tichmu.liang"
                },
                {
                    "uid": 15795,
                    "username": "ez.miao"
                },
                {
                    "uid": 737181,
                    "username": "lemon.xie"
                }
            ]
        },
        {
            "name": "北二组",
            "is_hide": 0,
            "gid": 2014,
            "father_id": 2261,
            "users": [
                {
                    "uid": 17369,
                    "username": "abby.zhou"
                },
                {
                    "uid": 17670,
                    "username": "gray.lu"
                },
                {
                    "uid": 1737,
                    "username": "bobo.wu"
                },
                {
                    "uid": 1902,
                    "username": "candy.gong"
                },
                {
                    "uid": 56525,
                    "username": "mei.zeng"
                },
                {
                    "uid": 56616,
                    "username": "alan.meng"
                },
                {
                    "uid": 10200,
                    "username": "jerry.deng"
                },
                {
                    "uid": 10928,
                    "username": "sun.lin"
                },
                {
                    "uid": 11432,
                    "username": "simon.huang"
                },
                {
                    "uid": 30142,
                    "username": "anna.bie"
                },
                {
                    "uid": 15818,
                    "username": "dick.gu"
                },
                {
                    "uid": 16198,
                    "username": "angela.liao"
                },
                {
                    "uid": 737182,
                    "username": "soul.xie"
                }
            ]
        },
        {
            "name": "南一组",
            "is_hide": 0,
            "gid": 2015,
            "father_id": 2260,
            "users": [
                {
                    "uid": 16728,
                    "username": "freedom.wang"
                },
                {
                    "uid": 17104,
                    "username": "nicet.xu"
                },
                {
                    "uid": 1551,
                    "username": "joey.shi"
                },
                {
                    "uid": 1709,
                    "username": "nancy.peng"
                },
                {
                    "uid": 741181,
                    "username": "can.wang"
                },
                {
                    "uid": 56593,
                    "username": "sunshini.zhang"
                },
                {
                    "uid": 56615,
                    "username": "sammy.zeng"
                },
                {
                    "uid": 56618,
                    "username": "harvey.xia"
                },
                {
                    "uid": 10147,
                    "username": "anna.liu"
                },
                {
                    "uid": 10225,
                    "username": "amy.zeng"
                },
                {
                    "uid": 10238,
                    "username": "youtu.zheng"
                },
                {
                    "uid": 12237,
                    "username": "junjay.zheng"
                },
                {
                    "uid": 30005,
                    "username": "bess.gan"
                },
                {
                    "uid": 14627,
                    "username": "roy.luo"
                },
                {
                    "uid": 735955,
                    "username": "efson.xu"
                },
                {
                    "uid": 736257,
                    "username": "wenyu.dong"
                },
                {
                    "uid": 736256,
                    "username": "kiter.xiao"
                }
            ]
        },
        {
            "name": "南三组",
            "is_hide": 0,
            "gid": 2016,
            "father_id": 2260,
            "users": [
                {
                    "uid": 17454,
                    "username": "jackie.fang"
                },
                {
                    "uid": 1601,
                    "username": "elma.xu"
                },
                {
                    "uid": 18399,
                    "username": "qiwen.fang"
                },
                {
                    "uid": 11640,
                    "username": "lida.peng"
                }
            ]
        },
        {
            "name": "微信小号组",
            "is_hide": 1,
            "gid": 2017,
            "father_id": 1352,
            "users": []
        },
        {
            "name": "非落地一组",
            "is_hide": 0,
            "gid": 2018,
            "father_id": 2261,
            "users": [
                {
                    "uid": 85333,
                    "username": "ally.li"
                },
                {
                    "uid": 86835,
                    "username": "howie.ma"
                },
                {
                    "uid": 87259,
                    "username": "sun.gong"
                },
                {
                    "uid": 56581,
                    "username": "jax.shi"
                },
                {
                    "uid": 56584,
                    "username": "kally.chang"
                },
                {
                    "uid": 746071,
                    "username": "guoliang.lin"
                },
                {
                    "uid": 76154,
                    "username": "zoer.zhou"
                },
                {
                    "uid": 11649,
                    "username": "jreey.qin"
                }
            ]
        },
        {
            "name": "非落地二组",
            "is_hide": 0,
            "gid": 2019,
            "father_id": 2260,
            "users": [
                {
                    "uid": 17881,
                    "username": "serrena.zheng"
                },
                {
                    "uid": 2007,
                    "username": "mary.yang"
                },
                {
                    "uid": 10956,
                    "username": "ann.gao"
                },
                {
                    "uid": 11604,
                    "username": "david.jiang"
                },
                {
                    "uid": 14806,
                    "username": "vencent.yang"
                },
                {
                    "uid": 14812,
                    "username": "jaky.zhu"
                }
            ]
        },
        {
            "name": "非落地三组",
            "is_hide": 1,
            "gid": 2020,
            "father_id": 1352,
            "users": []
        },
        {
            "name": "约前管家一组",
            "is_hide": 1,
            "gid": 2021,
            "father_id": 1352,
            "users": []
        },
        {
            "name": "约前管家二组",
            "is_hide": 1,
            "gid": 2022,
            "father_id": 1352,
            "users": []
        },
        {
            "name": "非落地开拓二组",
            "is_hide": 0,
            "gid": 2023,
            "father_id": 1988,
            "users": []
        },
        {
            "name": "华野队",
            "is_hide": 0,
            "gid": 2024,
            "father_id": 2023,
            "users": [
                {
                    "uid": 92749,
                    "username": "porter.wu"
                },
                {
                    "uid": 92751,
                    "username": "sugar.yang"
                }
            ]
        },
        {
            "name": "野狼队",
            "is_hide": 0,
            "gid": 2025,
            "father_id": 2023,
            "users": []
        },
        {
            "name": "青岛分公司",
            "is_hide": 0,
            "gid": 2026,
            "father_id": 2198,
            "users": [
                {
                    "uid": 1405,
                    "username": "vernon.zhu"
                },
                {
                    "uid": 743547,
                    "username": "yongxu.sun"
                },
                {
                    "uid": 745534,
                    "username": "quanfa.zhang"
                }
            ]
        },
        {
            "name": "廊坊分公司",
            "is_hide": 0,
            "gid": 2027,
            "father_id": 2197,
            "users": [
                {
                    "uid": 56638,
                    "username": "frank.kang"
                }
            ]
        },
        {
            "name": "惠州分公司",
            "is_hide": 0,
            "gid": 2028,
            "father_id": 2201,
            "users": []
        },
        {
            "name": "珠海分公司",
            "is_hide": 0,
            "gid": 2029,
            "father_id": 2201,
            "users": []
        },
        {
            "name": "宁波分公司",
            "is_hide": 0,
            "gid": 2030,
            "father_id": 2200,
            "users": []
        },
        {
            "name": "徐州分公司",
            "is_hide": 0,
            "gid": 2031,
            "father_id": 2198,
            "users": [
                {
                    "uid": 78,
                    "username": "king.zeng"
                }
            ]
        },
        {
            "name": "扬州分公司",
            "is_hide": 0,
            "gid": 2032,
            "father_id": 2199,
            "users": []
        },
        {
            "name": "赣州分公司",
            "is_hide": 0,
            "gid": 2033,
            "father_id": 2201,
            "users": []
        },
        {
            "name": "尖刀队",
            "is_hide": 1,
            "gid": 2034,
            "father_id": 1676,
            "users": []
        },
        {
            "name": "APP产品组",
            "is_hide": 1,
            "gid": 2035,
            "father_id": 1366,
            "users": []
        },
        {
            "name": "核算结算客服产品组",
            "is_hide": 1,
            "gid": 2036,
            "father_id": 1366,
            "users": []
        },
        {
            "name": "交付组",
            "is_hide": 0,
            "gid": 2037,
            "father_id": 2169,
            "users": [
                {
                    "uid": 65825,
                    "username": "jeremy.liang"
                },
                {
                    "uid": 11197,
                    "username": "kevin.ye"
                },
                {
                    "uid": 13810,
                    "username": "dana.huang"
                },
                {
                    "uid": 96116,
                    "username": "freeman.zhang"
                },
                {
                    "uid": 14498,
                    "username": "crazyking.wang"
                },
                {
                    "uid": 16317,
                    "username": "milly.chen"
                }
            ]
        },
        {
            "name": "BD支撑组",
            "is_hide": 0,
            "gid": 2038,
            "father_id": 2169,
            "users": [
                {
                    "uid": 18302,
                    "username": "shuai.pan"
                },
                {
                    "uid": 13808,
                    "username": "amos.tong"
                },
                {
                    "uid": 15183,
                    "username": "darren.jiang"
                }
            ]
        },
        {
            "name": "无锡展厅运营组",
            "is_hide": 0,
            "gid": 2039,
            "father_id": 1571,
            "users": []
        },
        {
            "name": "济南分公司",
            "is_hide": 0,
            "gid": 2040,
            "father_id": 2198,
            "users": []
        },
        {
            "name": "衡阳分公司",
            "is_hide": 0,
            "gid": 2041,
            "father_id": 2202,
            "users": [
                {
                    "uid": 745799,
                    "username": "chow.zhou"
                }
            ]
        },
        {
            "name": "石家庄分公司",
            "is_hide": 0,
            "gid": 2042,
            "father_id": 2197,
            "users": [
                {
                    "uid": 737803,
                    "username": "adler.kang"
                }
            ]
        },
        {
            "name": "哈尔滨分公司",
            "is_hide": 0,
            "gid": 2043,
            "father_id": 2197,
            "users": []
        },
        {
            "name": "长春分公司",
            "is_hide": 0,
            "gid": 2044,
            "father_id": 2197,
            "users": [
                {
                    "uid": 89497,
                    "username": "harvey.li"
                }
            ]
        },
        {
            "name": "中山分公司",
            "is_hide": 0,
            "gid": 2045,
            "father_id": 2201,
            "users": []
        },
        {
            "name": "嘉兴分公司",
            "is_hide": 0,
            "gid": 2046,
            "father_id": 2200,
            "users": []
        },
        {
            "name": "南通分公司",
            "is_hide": 0,
            "gid": 2047,
            "father_id": 2199,
            "users": []
        }
    ],
    "service": "com.permission",
    "esid": "e-293798912"
}
    success_list = response_json.get('success')

    gid2_list = list()
    for group in success_list:
        users = list()
        if group.get('gid') == 1722:
            users = group.get('users')
            for user in users:
                user_list.append(user)
        elif group.get('father_id') == 1722:
            gid2_list.append(group.get('gid'))
            users = group.get('users')
            for user in users:
                user_list.append(user)
    
    print(len(user_list))
    print(len(gid2_list))

    gid3_list = list()
    if len(gid2_list) == 0:
        # print(user_list)
        return user_list
    for group in success_list:
        father_id = group.get('father_id')
        if gid2_list.__contains__(father_id):
            users = group.get('users')
            for user in users:
                user_list.append(user)
            gid3_list.append(group.get('gid'))

    print(len(user_list))
    print(len(gid3_list))

    gid4_list = list()
    if len(gid3_list) == 0:
        # print(user_list)
        return user_list
    for group in success_list:
        father_id = group.get('father_id')
        if gid3_list.__contains__(father_id):
            users = group.get('users')
            for user in users:
                user_list.append(user)
            gid4_list.append(group.get('gid'))

    print(len(user_list))
    print(len(gid4_list))

    gid5_list = list()
    if len(gid4_list) == 0:
        # print(user_list)
        return user_list
    for group in success_list:
        father_id = group.get('father_id')
        if gid4_list.__contains__(father_id):
            users = group.get('users')
            for user in users:
                user_list.append(user)
            gid5_list.append(group.get('gid'))

    print(len(user_list))
    print(len(gid5_list))

    gid6_list = list()
    if len(gid5_list) == 0:
        # print(user_list)
        return user_list
    for group in success_list:
        father_id = group.get('father_id')
        if gid5_list.__contains__(father_id):
            users = group.get('users')
            for user in users:
                user_list.append(user)
            gid6_list.append(group.get('gid'))
    
    print(len(user_list))
    print(len(gid6_list))

    gid7_list = list()
    if len(gid6_list) == 0:
        # print(user_list)
        return user_list

def get_uid_from_users(user_list):
    uid_list = list()
    for user in user_list:
        uid_list.append(str(user.get('uid')))
    so_id_string = ",".join(uid_list)
    return so_id_string

def wash_data(uid_list_str):
    connection = pymysql.connect(host='192.168.1.121',
                                 port=3306,
                                 user='to8tomaster_java',
                                 password='for_javacrm_connect',
                                 db='to8to',
                                 charset='utf8mb4')
    # connection = mysql.connector.connect(user='to8tomaster_java', password='for_javacrm_connect',
    #                                      host='192.168.1.121', database='to8to', use_unicode=False, buffered=True)
    # connection = mysql.connector.connect(user='tuorixsy', password='1982425',
    #                                      host='192.168.3.199', database='to8to', use_unicode=False, buffered=True)

    cursor = connection.cursor()
    try:
        sql = 'SELECT uid, devicecode FROM to8to_user_info WHERE uid IN (%s)' % (uid_list_str)
        print('\n\n执行sql: %s' % (sql))
        cursor.execute(sql)
        result = cursor.fetchall()
        print('\n\n更新前数据: %s' % (result))
    except pymysql.err.Error as e:
        print(e)

    try:
        sql = 'UPDATE to8to_user_info SET devicecode = 0 WHERE uid in (%s)' % (uid_list_str)
        print('\n\n执行sql: %s' % (sql))
        cursor.execute(sql)
    except pymysql.err.Error as e:
        print(e)

    try:
        sql = 'SELECT uid, devicecode FROM to8to_user_info WHERE uid IN (%s)' % (uid_list_str)
        print('\n\n执行sql: %s' % (sql))
        cursor.execute(sql)
        result = cursor.fetchall()
        print('\n\n更新后数据: %s' % (result))
    except pymysql.err.Error as e:
        print(e)
        
def main():
    uid_list_str = get_uid_from_users(get_all_zj_users())
    wash_data(uid_list_str)

if __name__ == '__main__':
    main()
