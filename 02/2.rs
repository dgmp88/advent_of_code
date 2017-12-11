fn string_to_vec(sheet: &str) -> Vec<Vec<f32>> {
    // Turn a string into a vec of vec of f32's
    let mut sheet_vec = Vec::new();
    for line in sheet.split("\n") {
        let mut line_vec = Vec::new();
        for num in line.split("\t") {
            let int = num.trim().parse::<f32>();
            match int {
                Ok(val) => line_vec.push(val),
                Err(_why) => {} ,
            }
        }
        sheet_vec.push(line_vec);
    }
    sheet_vec
}
fn checksum (sheet: Vec<Vec<f32>>) -> f32 {
    let mut tot = 0.0;
    for row in &sheet {
        let mut min = row[0];
        let mut max = row[0];
        for val in row {
            if val > &max {
                max = val.clone();
            } else if val < &min {
                min = val.clone();
            }
        }
        tot += max - min;
    }
    tot
}

fn checksum_2 (sheet: Vec<Vec<f32>>) -> f32 {
    let mut tot = 0.0;
    for row in &sheet {
        tot += get_division(row);
    }
    tot
}

fn get_division(row: &Vec<f32>) -> f32{
    for i in row {
        for j in row {
            if i != j {
                let div = i / j;
                if div % 1.0 == 0.0 {
                    return div;
                }
            }
        }
    }
    assert!(false, "Failed to find divisors");
    0.0
}

fn test() {
    let sheet_str = "5	1	  9	   5
7	5	3
2	4	6	8";
    let sheet = string_to_vec(sheet_str);

    let csum = checksum(sheet);
    assert!(csum == 18.0, "Sum should be 18, it is {}", csum);
}
fn test_2() {
    let sheet_str = "5	 9	 2	 8
    9	4	7	3
    3	8	6	5";
    let sheet = string_to_vec(sheet_str);
    let csum = checksum_2(sheet);
    assert!(csum == 9.0, "Sum should be 18, it is {}", csum);

}

fn get_sheet() -> Vec<Vec<f32>> {
    let sheet = "1224	926	1380	688	845	109	118	88	1275	1306	91	796	102	1361	27	995
1928	2097	138	1824	198	117	1532	2000	1478	539	1982	125	1856	139	475	1338
848	202	1116	791	1114	236	183	186	150	1016	1258	84	952	1202	988	866
946	155	210	980	896	875	925	613	209	746	147	170	577	942	475	850
1500	322	43	95	74	210	1817	1631	1762	128	181	716	171	1740	145	1123
3074	827	117	2509	161	206	2739	253	2884	248	3307	2760	2239	1676	1137	3055
183	85	143	197	243	72	291	279	99	189	30	101	211	209	77	198
175	149	259	372	140	250	168	142	146	284	273	74	162	112	78	29
169	578	97	589	473	317	123	102	445	217	144	398	510	464	247	109
3291	216	185	1214	167	495	1859	194	1030	3456	2021	1622	3511	222	3534	1580
2066	2418	2324	93	1073	82	102	538	1552	962	91	836	1628	2154	2144	1378
149	963	1242	849	726	1158	164	1134	658	161	1148	336	826	1303	811	178
3421	1404	2360	2643	3186	3352	1112	171	168	177	146	1945	319	185	2927	2289
543	462	111	459	107	353	2006	116	2528	56	2436	1539	1770	125	2697	2432
1356	208	5013	4231	193	169	3152	2543	4430	4070	4031	145	4433	4187	4394	1754
5278	113	4427	569	5167	175	192	3903	155	1051	4121	5140	2328	203	5653	3233";

    let res = string_to_vec(sheet);
    res
}

fn one() {
    let res = checksum(get_sheet());
    println!("Result 1 is {}", res);
}

fn two() {
    let res = checksum_2(get_sheet());
    println!("Result 2 is {}", res);
}

fn main() {
    test();
    one();
    test_2();
    two();
}


