data_hash_map = {"/": {"parent": None, "total": 0}}
with open("input.txt") as file:
    # This will store the whole directory map and total value
    parent = None
    current_dir = "/"
    for line in file:
        line = line.strip("\n")
        if line.startswith("$") and (len(line.split(" ")) == 3):
            if line.split(" ")[2] == "..":
                current_dir = data_hash_map[current_dir]["parent"]
            else:
                current_dir = line.split(" ")[2]

        elif line.startswith("$") and line.endswith("ls"):
            pass
        elif line.startswith("dir"):
            data_hash_map[line.split(" ")[1]] = {
                "parent": current_dir,
                "total": 0,
            }

        elif (not line.startswith("dir")) and (not line.startswith("$")):
            data_hash_map[current_dir][line.split(" ")[1]] = line.split(" ")[0]

print(data_hash_map)
# loop over the items
def traverse_and_calculate(data):
    total = 0
    for (i, v) in data.items():
        if (i != "parent") and (i != "total"):
            total += int(v)
    return int(total)


# traverse and calculate total
for (item, value) in data_hash_map.items():
    total = traverse_and_calculate(value)
    data_hash_map[item]["total"] = total
    if data_hash_map[item]["parent"] != None:
        parent = data_hash_map[item]["parent"]
        idx = 0
        # print(parent)
        while parent is not None:
            # print(parent)
            data_hash_map[parent]["total"] += total
            # print(data_hash_map[parent]["total"])
            parent = data_hash_map[parent]["parent"]
            # print(parent, "parent")

# final calculation
final_result = 0
for (item, value) in data_hash_map.items():
    total = data_hash_map[item]["total"]
    if total <= 100000:
        final_result += total

print(final_result)

{
    "/": {"parent": None, "total": 0, "hznrlfhh.tnz": "284723"},
    "dpllhlcv": {"parent": "/", "total": 0, "bplz.rdp": "11223"},
    "mgjdlmrz": {"parent": "/", "total": 0, "dng.qrc": "79173"},
    "njstc": {
        "parent": "/",
        "total": 0,
        "bplz.rdp": "70592",
        "ccdp.lpw": "100122",
        "lcr.mqp": "21922",
        "rwdnfc.zqq": "9581",
    },
    "nzwbc": {"parent": "grq", "total": 0, "vzc": "12818"},
    "qzzfvdh": {"parent": "/", "total": 0, "dgpfcftj.fbr": "102585"},
    "smvhphf": {"parent": "/", "total": 0, "dvtblw.wsr": "202817"},
    "gpmlznd": {
        "parent": "dpllhlcv",
        "total": 0,
        "nzwbc.rgv": "83678",
        "wpglzlrf.htl": "94635",
    },
    "pgcctrb": {"parent": "dpllhlcv", "total": 0},
    "wmsl": {
        "parent": "snjv",
        "total": 0,
        "nzwbc.pmp": "84076",
        "rrrj.gph": "196119",
        "ttbswbhs.ffs": "104986",
    },
    "lwzcss": {"parent": "gpmlznd", "total": 0},
    "rhdllvm": {"parent": "gpmlznd", "total": 0},
    "bttplh": {"parent": "lwzcss", "total": 0},
    "rzj": {"parent": "bttplh", "total": 0, "nzwbc.psj": "59866"},
    "mvqfrq": {"parent": "rhdllvm", "total": 0, "prvl": "41266"},
    "dgpfcftj": {"parent": "fvwm", "total": 0, "qqb.qmd": "214069"},
    "hhtztpm": {
        "parent": "wmsl",
        "total": 0,
        "djfbm.djl": "196378",
        "ltnwbvg.rqz": "203856",
        "mjrlm": "266242",
    },
    "tzjthwc": {
        "parent": "grq",
        "total": 0,
        "dgpfcftj": "54762",
        "gbt.whg": "179432",
        "whr.jqn": "220002",
    },
    "ngjd": {"parent": "hhtztpm", "total": 0, "mjrlm": "289546"},
    "lhccf": {"parent": "tzjthwc", "total": 0, "rrrj.wzl": "100347"},
    "wgnhhl": {"parent": "tzjthwc", "total": 0, "rrrj": "120460"},
    "zfwffjn": {"parent": "lhccf", "total": 0, "rrrj.jcz": "23992"},
    "mrd": {"parent": "zfwffjn", "total": 0, "qqwlrbsw.zfn": "139407"},
    "vnwpddtf": {
        "parent": "zfwffjn",
        "total": 0,
        "dgpfcftj.wpm": "287771",
        "qqb.qmd": "59212",
    },
    "zpldfrj": {"parent": "wmsl", "total": 0, "qljrrlm.clw": "180679"},
    "fnfw": {
        "parent": "mgjdlmrz",
        "total": 0,
        "bplz.rdp": "263282",
        "ttbswbhs.ffs": "177780",
        "tzjthwc.wlq": "28452",
        "wmsl.rmd": "19548",
    },
    "hwb": {
        "parent": "mgjdlmrz",
        "total": 0,
        "dshmsgj.cnd": "44576",
        "tdcgvdv.phs": "70710",
    },
    "nfqzjs": {"parent": "mgjdlmrz", "total": 0, "tfwmgdj": "18103"},
    "qdgplmrt": {"parent": "mgjdlmrz", "total": 0, "mjrlm": "163549"},
    "znrnj": {
        "parent": "mgjdlmrz",
        "total": 0,
        "mzbpjgd.lmp": "53146",
        "vmtdc": "202250",
    },
    "bhjm": {
        "parent": "fnfw",
        "total": 0,
        "dgpfcftj": "57561",
        "hwsjhwvf.rmv": "170692",
    },
    "dhsvtfc": {
        "parent": "fnfw",
        "total": 0,
        "dgpfcftj": "201361",
        "jjjjwcw": "291508",
        "pfdvf.pmj": "445",
        "qpc.gsw": "135732",
        "wlgrtn.mjb": "115597",
    },
    "hlh": {"parent": "fnfw", "total": 0, "rrrj.mfv": "96676"},
    "bpl": {
        "parent": "bhjm",
        "total": 0,
        "fmbpzn": "275227",
        "mjztf.nlg": "9798",
        "nzwbc": "190388",
    },
    "glplnd": {
        "parent": "bhjm",
        "total": 0,
        "bplz.rdp": "147261",
        "hznrlfhh.tnz": "267191",
    },
    "rrrj": {
        "parent": "snjv",
        "total": 0,
        "bdgws": "277036",
        "dgpfcftj.zgt": "269322",
        "qqb.qmd": "33872",
    },
    "tlltjd": {"parent": "bhjm", "total": 0, "swqcsnw": "58096"},
    "btpglc": {"parent": "bpl", "total": 0, "rrrj.rhl": "276105"},
    "hqmw": {"parent": "tzjthwc", "total": 0, "mchnt.pls": "163168"},
    "fwdw": {
        "parent": "rrrj",
        "total": 0,
        "fgtfj.pnc": "166347",
        "mspn.wcw": "140486",
        "nzwbc.dhb": "26602",
        "qqb.qmd": "81490",
    },
    "tnpjsgnq": {"parent": "rrrj", "total": 0},
    "tpvttzv": {"parent": "rrrj", "total": 0},
    "dqtbltwp": {"parent": "dgpfcftj", "total": 0, "tzjthwc.gnr": "27856"},
    "gbddb": {"parent": "tnpjsgnq", "total": 0, "qqb.qmd": "1587"},
    "gpqssnq": {"parent": "tnpjsgnq", "total": 0, "fmjpw.mtp": "33979"},
    "bqvzmb": {
        "parent": "tpvttzv",
        "total": 0,
        "fdhjztlv": "79211",
        "wgvqvdp.pzp": "72991",
    },
    "cwbq": {
        "parent": "dhsvtfc",
        "total": 0,
        "hznrlfhh.tnz": "173860",
        "mjrlm": "97790",
    },
    "ccgdn": {
        "parent": "cwbq",
        "total": 0,
        "fgmntg.crb": "46502",
        "nwj.fht": "11175",
        "qqb.qmd": "208129",
    },
    "gcfbqh": {
        "parent": "cwbq",
        "total": 0,
        "crmpsc.rbf": "92250",
        "tzjthwc": "284234",
    },
    "qtfhz": {
        "parent": "cwbq",
        "total": 0,
        "hznrlfhh.tnz": "164311",
        "mjrlm": "137031",
    },
    "tpgj": {"parent": "cwbq", "total": 0, "jdpv.fpw": "210570"},
    "tph": {"parent": "cwbq", "total": 0},
    "blnzrjm": {
        "parent": "ccgdn",
        "total": 0,
        "gvs": "121398",
        "pdppzscr.vph": "201215",
        "smwrnw.hqp": "3861",
        "wzccnw.lsc": "220659",
    },
    "fwdpw": {"parent": "ccgdn", "total": 0, "prhjf": "28780"},
    "nbldsrfq": {"parent": "ccgdn", "total": 0, "dcrhr": "57352"},
    "wpj": {"parent": "ccgdn", "total": 0, "jmdn.bzh": "51243"},
    "pwj": {
        "parent": "blnzrjm",
        "total": 0,
        "bwj.ntc": "279141",
        "jvqwhwmh.brq": "15325",
    },
    "hptp": {"parent": "tph", "total": 0, "qqb.qmd": "272964", "svrcpb": "147435"},
    "psndpb": {
        "parent": "wmsl",
        "total": 0,
        "lszgqt": "272771",
        "mjrlm": "136189",
        "qqb.qmd": "166606",
    },
    "dbm": {"parent": "psndpb", "total": 0},
    "fbmfpndf": {"parent": "psndpb", "total": 0, "bplz.rdp": "186758"},
    "fstgbcrc": {
        "parent": "psndpb",
        "total": 0,
        "hznrlfhh.tnz": "4975",
        "mjrlm": "59093",
        "qqb.qmd": "279246",
    },
    "vptjzdt": {"parent": "psndpb", "total": 0, "ttbswbhs.ffs": "117403"},
    "ffmrngmj": {"parent": "nzwbc", "total": 0, "nrwrptz.cmp": "299742"},
    "cdgrjlz": {
        "parent": "dgpfcftj",
        "total": 0,
        "dpnzsq.dbd": "89863",
        "mjrlm": "259686",
        "qqb.qmd": "50165",
    },
    "jnffc": {
        "parent": "njstc",
        "total": 0,
        "vbvpzw.rst": "54279",
        "vzshqq.qpb": "147514",
    },
    "jnrrwt": {"parent": "njstc", "total": 0, "bplz.rdp": "51615"},
    "mdts": {"parent": "njstc", "total": 0, "ttbswbhs.ffs": "191614"},
    "zchc": {"parent": "njstc", "total": 0},
    "fvmgmn": {"parent": "jnrrwt", "total": 0, "sntlcs.vms": "159538"},
    "wjrqnlr": {"parent": "jnrrwt", "total": 0, "mjrlm": "135325", "qqb.qmd": "94135"},
    "dvcqnv": {"parent": "wjrqnlr", "total": 0, "mjrlm": "66408"},
    "jnjzlhhw": {"parent": "wjrqnlr", "total": 0, "bplz.rdp": "89668"},
    "btcjthr": {"parent": "jnjzlhhw", "total": 0, "zjf.fqt": "280405"},
    "sbcwwvj": {"parent": "btcjthr", "total": 0},
    "mfbhtb": {"parent": "nzwbc", "total": 0, "sjrwtjcq": "21538"},
    "nbdn": {
        "parent": "nzwbc",
        "total": 0,
        "bplz.rdp": "120432",
        "hjsv": "180737",
        "mjrlm": "295982",
        "vzjtg.hhp": "13218",
        "zjwf.spw": "1332",
    },
    "nzw": {"parent": "nzwbc", "total": 0, "hfbptj.rsq": "135129"},
    "zcv": {
        "parent": "nzwbc",
        "total": 0,
        "dntqvr.snf": "256838",
        "rrrj.lvd": "293181",
    },
    "ltrg": {"parent": "dgpfcftj", "total": 0},
    "rvt": {"parent": "wmsl", "total": 0, "nzwbc": "232235"},
    "rscwnwt": {
        "parent": "nbdn",
        "total": 0,
        "fnvfrbzg.wmw": "268727",
        "jgfvpmp": "155540",
        "rrrj": "242598",
        "vqqqmg.dss": "47339",
    },
    "nhzg": {"parent": "nzw", "total": 0, "tzjthwc.gsl": "219375"},
    "qshfn": {"parent": "nzw", "total": 0, "whsdfns": "279385", "wmsl.tpl": "141044"},
    "pnjhczqg": {"parent": "qshfn", "total": 0, "rlgtn.jvh": "141321"},
    "wrh": {"parent": "pnjhczqg", "total": 0, "sfvrld.nsz": "143304"},
    "lnhmfb": {"parent": "tzjthwc", "total": 0},
    "dzzdvmtl": {"parent": "lnhmfb", "total": 0},
    "ttnm": {
        "parent": "lnhmfb",
        "total": 0,
        "hznrlfhh.tnz": "272667",
        "wmsl.ggr": "251551",
        "wmsl.phl": "97289",
    },
    "mrg": {"parent": "dzzdvmtl", "total": 0, "rrrj.lnh": "174378"},
    "cwsqwt": {
        "parent": "zcv",
        "total": 0,
        "bbrgtfh.zmf": "141770",
        "mjrlm": "100359",
        "qqb.qmd": "96547",
        "ttbswbhs.ffs": "176620",
    },
    "nbq": {
        "parent": "zcv",
        "total": 0,
        "bwdvjv.gwq": "132140",
        "rrrj": "248867",
        "sjtsjgrb": "226784",
        "tjh.vft": "94475",
        "tzjthwc.rgb": "149501",
    },
    "nzbdsvt": {"parent": "zcv", "total": 0, "ttbswbhs.ffs": "89301"},
    "gbjtzhj": {"parent": "nbq", "total": 0, "rrrj.msh": "43689"},
    "mfsr": {"parent": "nbq", "total": 0, "sntz.lqw": "30068"},
    "tch": {"parent": "mfsr", "total": 0},
    "zzgtsqvh": {"parent": "mfsr", "total": 0, "tzjthwc.mql": "289069"},
    "vgnlftjr": {
        "parent": "qzzfvdh",
        "total": 0,
        "mjrlm": "29769",
        "wmsl.nhr": "53024",
        "wps.hhq": "123863",
    },
    "vjqzf": {
        "parent": "qzzfvdh",
        "total": 0,
        "lgrst.fhc": "45701",
        "spdrmtbd.pnd": "265249",
        "ttbswbhs.ffs": "182349",
    },
    "zhmgmmv": {"parent": "qzzfvdh", "total": 0, "qtjnmzrd.grm": "165656"},
    "lfpltbmd": {"parent": "nzwbc", "total": 0, "frtspbh": "59516"},
    "lmnvgrm": {"parent": "nzwbc", "total": 0, "nwc.qbd": "12367"},
    "qnfp": {
        "parent": "nzwbc",
        "total": 0,
        "ddbcjwg.wqc": "78470",
        "qrwct.rvp": "254734",
        "wmsl.wgv": "95613",
    },
    "wdn": {
        "parent": "nzwbc",
        "total": 0,
        "gpp.qdd": "220196",
        "jsjcvvmd.mdc": "71184",
        "rrrj.cqm": "228140",
    },
    "ldq": {"parent": "qnfp", "total": 0, "ttbswbhs.ffs": "268677"},
    "ljv": {
        "parent": "qnfp",
        "total": 0,
        "gjddvvbs.zjq": "184758",
        "mjrlm": "278919",
        "nzwbc.fsf": "241428",
    },
    "wfqbv": {
        "parent": "wmsl",
        "total": 0,
        "tgrlfscv.vbn": "268503",
        "vwlcnm.wqq": "222733",
    },
    "wdfwp": {
        "parent": "ljv",
        "total": 0,
        "jnhpmp": "100960",
        "sfhjbnq.jpr": "204739",
        "twrzzn.tpm": "110857",
    },
    "mnd": {"parent": "wmsl", "total": 0},
    "cjrtl": {
        "parent": "tzjthwc",
        "total": 0,
        "frfb.flq": "157605",
        "gqtprzlg": "182254",
        "ttbswbhs.ffs": "86395",
    },
    "cmqzqrc": {"parent": "tzjthwc", "total": 0},
    "gmlgztg": {
        "parent": "tzjthwc",
        "total": 0,
        "bplz.rdp": "234781",
        "nzwbc.mgl": "29314",
        "qqb.qmd": "86928",
        "rrrj.qlm": "262374",
    },
    "qflmtrgh": {"parent": "tzjthwc", "total": 0},
    "snjv": {"parent": "tzjthwc", "total": 0, "nzwbc": "92025"},
    "vsq": {
        "parent": "tzjthwc",
        "total": 0,
        "hznrlfhh.tnz": "136431",
        "mrrc.tst": "195767",
    },
    "lldcwcf": {"parent": "cjrtl", "total": 0, "bplz.rdp": "279487", "djzs": "229071"},
    "dnfztwvj": {"parent": "wmsl", "total": 0, "hznrlfhh.tnz": "211224"},
    "bsfqcv": {"parent": "cmqzqrc", "total": 0, "ltzblpc": "62520"},
    "pzfnlzbj": {"parent": "dgpfcftj", "total": 0, "dgpfcftj.ffm": "190720"},
    "wrm": {
        "parent": "qflmtrgh",
        "total": 0,
        "jzgqvthh": "13708",
        "mlwflb": "138652",
        "szfzs.clj": "145161",
        "ttbswbhs.ffs": "297793",
    },
    "wftzbw": {"parent": "rrrj", "total": 0},
    "chzs": {"parent": "wftzbw", "total": 0},
    "dfhzcft": {"parent": "chzs", "total": 0, "mjrlm": "93504"},
    "grq": {"parent": "snjv", "total": 0, "jzccjh.lsl": "189188", "pngngj": "97611"},
    "wjcjqc": {"parent": "grq", "total": 0, "ttbswbhs.ffs": "258155"},
    "cfwvmwr": {"parent": "tzjthwc", "total": 0, "pfgmbsjd": "227691"},
    "njsfv": {
        "parent": "tzjthwc",
        "total": 0,
        "fpjqqcsp.czm": "39114",
        "mjrlm": "289813",
        "qqb.qmd": "279549",
    },
    "fsqdnl": {"parent": "rrrj", "total": 0, "zczcgq.lbb": "250732"},
    "zmvrrdps": {"parent": "wmsl", "total": 0, "wmsl.mpg": "170723"},
    "gnnstzc": {
        "parent": "vjqzf",
        "total": 0,
        "lbqh.pst": "105525",
        "rrrj.hlm": "13456",
        "vll.cft": "62170",
    },
    "fvwm": {"parent": "zhmgmmv", "total": 0},
}
