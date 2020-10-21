getBestVaras(vara_id, 10, (result)=>{
    console.log('=== '+JSON.stringify(result))
    var groups = ['distribuição','conclusão','despacho','decisão','julgamento','trânsito em julgado','baixa ou arquivamento']
    var time_distribuicao = ["distribuição"]
    var time_conclusao = ["conclusão"]
    var time_despacho = ["despacho"]
    var time_decisao = ["decisão"]
    var time_julgamento = ["julgamento"]
    var time_transito_em_julgado = ["trânsito em julgado"]
    var time_baixa_ou_arquivamento = ["baixa ou arquivamento"]
    result.forEach(json => {
        /* if(time_distribuicao.length == 0){
            time_distribuicao.push(json.name)
            time_conclusao.push(json.name)
            time_despacho.push(json.name)
            time_decisao.push(json.name)
            time_julgamento.push(json.name)
            time_transito_em_julgado.push(json.name)
            time_baixa_ou_arquivamento.push(json.name)
        } */


        if(json.time_distribuicao && json.time_distribuicao != null)
            time_distribuicao.push(json.time_distribuicao)
        else
            time_distribuicao.push(0)
        if(json.time_conclusao && json.time_conclusao != null)
            time_conclusao.push(json.time_conclusao)
        else
            time_conclusao.push(0)
        if(json.time_despacho && json.time_despacho != null)
            time_despacho.push(json.time_despacho)
        else
            time_despacho.push(0)
        if(json.time_decisao && json.time_decisao != null)
            time_decisao.push(json.time_decisao)
        else
            time_decisao.push(0)
        if(json.time_julgamento && json.time_julgamento != null)
            time_julgamento.push(json.time_julgamento)
        else
            time_julgamento.push(0)
        if(json.time_transito_em_julgado && json.time_transito_em_julgado != null)
            time_transito_em_julgado.push(json.time_transito_em_julgado)
        else
            time_transito_em_julgado.push(0)
        if(json.time_baixa_ou_arquivamento && json.time_baixa_ou_arquivamento != null)
            time_baixa_ou_arquivamento.push(json.time_baixa_ou_arquivamento)
        else
            time_baixa_ou_arquivamento.push(0)
    });
    var chart = c3.generate({
        data: {
            columns: [time_distribuicao, time_conclusao, time_despacho, time_decisao,
                time_julgamento, time_transito_em_julgado, time_baixa_ou_arquivamento],
            type: 'bar',
            groups: [groups]
            //groups: [result.map(court => court.name)]
        },
        grid: {
            y: {
                lines: [{value:0}]
            }
        },
        tooltip: {
            format: {
                title: function (d) { return result[d].name; }
            }
        }
      });
})


  