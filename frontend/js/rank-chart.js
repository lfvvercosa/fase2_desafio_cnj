
getBestVaras(vara_id, 10, (result)=>{
    var groups = ['Distribuição','Conclusão','Despacho','Decisão','Julgamento','Trânsito em julgado','Baixa ou arquivamento', 'Audiencia', 'Citação', 'Outros']
    var time_distribuicao = ["Distribuição"]
    var time_conclusao = ["Conclusão"]
    var time_despacho = ["Despacho"]
    var time_decisao = ["Decisão"]
    var time_julgamento = ["Julgamento"]
    var time_transito_em_julgado = ["Trânsito em julgado"]
    var time_baixa_ou_arquivamento = ["Baixa ou arquivamento"]
    var time_audiencia = ["Audiencia"]
    var time_citacao = ["Citação"]
    var time_outros = ["Outros"]
    result.forEach(json => {
        console.log(json)
        if(json.time_distribuicao && json.time_distribuicao != null)
            time_distribuicao.push(getValidValue(json.time_distribuicao))
        else
            time_distribuicao.push(0)
        if(json.time_conclusao && json.time_conclusao != null)
            time_conclusao.push(getValidValue(json.time_conclusao))
        else
            time_conclusao.push(0)
        if(json.time_despacho && json.time_despacho != null)
            time_despacho.push(getValidValue(json.time_despacho))
        else
            time_despacho.push(0)
        if(json.time_decisao && json.time_decisao != null)
            time_decisao.push(getValidValue(json.time_decisao))
        else
            time_decisao.push(0)
        if(json.time_julgamento && json.time_julgamento != null)
            time_julgamento.push(getValidValue(json.time_julgamento))
        else
            time_julgamento.push(0)
        if(json.time_transito_em_julgado && json.time_transito_em_julgado != null)
            time_transito_em_julgado.push(getValidValue(json.time_transito_em_julgado))
        else
            time_transito_em_julgado.push(0)
        if(json.time_baixa_ou_arquivamento && json.time_baixa_ou_arquivamento != null)
            time_baixa_ou_arquivamento.push(getValidValue(json.time_baixa_ou_arquivamento))
        else
            time_baixa_ou_arquivamento.push(0)
        if(json.time_audiencia && json.audiencia != null)
            time_audiencia.push(getValidValue(json.audiencia))
        else
            time_audiencia.push(0)
        if(json.time_citacao && json.citacao != null)
            time_citacao.push(getValidValue(json.citacao))
        else
            time_citacao.push(0)
        if(json.time_outros && json.outros!= null)
            time_outros.push(getValidValue(json.outros))
        else
            time_outros.push(0)
    });
    var chart = c3.generate({
        data: {
            columns: [time_distribuicao, time_conclusao, time_despacho, time_decisao,
                time_julgamento, time_transito_em_julgado, time_baixa_ou_arquivamento, time_audiencia
            , time_citacao, time_outros],
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
        },
        axis: {
          y: {
            label: {
              text: 'Número de dias',
              position: 'outer-middle'
            }
          }
        }
      });
})

function getValidValue(value) {
    if(value == -1)
        value = 0
    return value
}

  