class Tile {
    constructor(Tile_name, type, number) {
      this.Tile_name = Tile_name;
      this.type = type;
      this.number = number;
    }
  }
let t0 = new Tile('t0','ore', 10)
let t1 = new Tile('t1','sheep', 2)
let t2 = new Tile('t2','wood', 9)
let t3 = new Tile('t3','grain', 11)
let t4 = new Tile('t4','brick', 6)
let t5 = new Tile('t5','sheep', 4)
let t6 = new Tile('t6','brick', 10)
let t7 = new Tile('t7','grain', 9)
let t8 = new Tile('t8','wood', 11)
let t9 = new Tile('t9','desert', 0)
let t10 = new Tile('t10','wood', 3)
let t11 = new Tile('t11','ore', 8)
let t12 = new Tile('t12','wood', 8)
let t13 = new Tile('t13','ore', 3)
let t14 = new Tile('t14','grain', 4)
let t15 = new Tile('t15','sheep', 5)
let t16 = new Tile('t16','brick', 5)
let t17 = new Tile('t17','grain', 6)
let t18 = new Tile('t18','sheep', 11)

class Vertex {
    constructor(settlement, edge) {
        this.settlement = settlement;
        this.edge = edge;
      }
}

let v0 = new Vertex("s0", [t0]);
let v1 = new Vertex("s0", [t1]);
let v2 = new Vertex('s2', [t2]);
let v3 = new Vertex('s3', [t0]);
let v4 = new Vertex('s4', [t0, t1]);
let v5 = new Vertex('s5', [t1, t2]);
let v6 = new Vertex('s6', [t2]);
let v7 = new Vertex('s7', [t0, t3]);
let v8 = new Vertex('s8', [t0, t1, t4]);
let v9 = new Vertex('s9', [t1, t2, t5]);
let v10 = new Vertex('s10', [t2, t6]);
let v11 = new Vertex('s11', [t3]);
let v12 = new Vertex('s12', [t0, t3, t4]);
let v13 = new Vertex('s13', [t1, t4, t5]);
let v14 = new Vertex('s14', [t2, t5, t6]);
let v15 = new Vertex('s15', [t6]);
let v16 = new Vertex('s16', [t3, t7]);
let v17 = new Vertex('s17', [t3, t4, t8]);
let v18 = new Vertex('s18', [t4, t5, t9]);
let v19 = new Vertex('s19', [t5, t6, t10]);
let v20 = new Vertex('s20', [t6, t11]);
let v21 = new Vertex('s21', [t7]);
let v22 = new Vertex('s22', [t3, t7, t8]);
let v23 = new Vertex('s23', [t4, t8, t9]);
let v24 = new Vertex('s24', [t5, t9, t10]);
let v25 = new Vertex('s25', [t6, t10, t11]);
let v26 = new Vertex('s26', [t11]);
let v27 = new Vertex('s27', [t7]);
let v28 = new Vertex('s28', [t7, t8, t12]);
let v29 = new Vertex('s29', [t8, t9, t13]);
let v30 = new Vertex('s30', [t9, t10, t14]);
let v31 = new Vertex('s31', [t10, t11, t15]);
let v32 = new Vertex('s32', [t11]);
let v33 = new Vertex('s33', [t7, t12]);
let v34 = new Vertex('s34', [t8, t12, t13]);
let v35 = new Vertex('s35', [t9, t13, t14]);
let v36 = new Vertex('s36', [t10, t14, t15]);
let v37 = new Vertex('s37', [t11, t15]);
let v38 = new Vertex('s38', [t12]);
let v39 = new Vertex('s39', [t12, t13, t16]);
let v40 = new Vertex('s40', [t13, t14, t17]);
let v41 = new Vertex('s41', [t14, t15, t18]);
let v42 = new Vertex('s42', [t15]);
let v43 = new Vertex('s43', [t12, t16]);
let v44 = new Vertex('s44', [t13, t16, t17]);
let v45 = new Vertex('s45', [t14, t17, t18]);
let v46 = new Vertex('s46', [t15, t18]);
let v47 = new Vertex('s47', [t16]);
let v48 = new Vertex('s48', [t16, t17]);
let v49 = new Vertex('s49', [t17, t18]);
let v50 = new Vertex('s50', [t18]);
let v51 = new Vertex('s51', [t16]);
let v52 = new Vertex('s52', [t17]);
let v53 = new Vertex('s53', [t18]);

const tiles = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18];
for (let x in tiles){
    if (tiles[x].number == 2){
        tiles[x].prob = 1/36;
    }
    if (tiles[x].number == 3){
        tiles[x].prob = 2/36;
    }
    if (tiles[x].number == 4){
        tiles[x].prob = 3/36;
    }
    if (tiles[x].number == 5){
        tiles[x].prob = 4/36;
    }
    if (tiles[x].number == 6){
        tiles[x].prob = 5/36;
    }
    if (tiles[x].number == 8){
        tiles[x].prob = 5/36;
    }if (tiles[x].number == 9){
        tiles[x].prob = 4/36;
    }if (tiles[x].number == 10){
        tiles[x].prob = 3/36;
    }
    if (tiles[x].number == 11){
        tiles[x].prob = 2/36;
    }
    if (tiles[x].number == 12){
        tiles[x].prob = 1/36;
    }
}
const vertices = [v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43, v44, v45, v46, v47, v48, v49, v50, v51, v52, v53];
for (let i in vertices){
    vertices[i].total = 0
    for (let j in i.edge){
        vertices[i].total += j.prob;
    }
}
best_settlement = [0, ''];
for (let k in vertices){
    if (k.total > best_settlement[0]){
        best_settlement[0] = k.total;
        best_settlement[1] = k.settlement;
    }
}

