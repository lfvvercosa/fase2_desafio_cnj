
getBestVaras(vara_id, selectedGroup.varas.length, (result)=>{
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
    setNeighborsChart(result)
    var best = result.slice(0,5)
    best.slice(0,5).forEach(json => {
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
    c3.generate({
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
                title: function (d) { return best[d].name; }
            }
        },
        axis: {
          y: {
            label: {
              text: 'Porcentagem',
              position: 'outer-middle'
            },
            max: 100,
            min: 0,
            padding: {top: 0, bottom: 0}
          }
        },
        bindto: "#chart_best"
      });
      
})

function setNeighborsChart(result) {
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
    var neighbors = findNeighbors(result)
    neighbors.forEach(json => {
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
    c3.generate({
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
                title: function (d) { return neighbors[d].name; }
            }
        },
        axis: {
          y: {
            label: {
              text: 'Porcentagem',
              position: 'outer-middle'
            },
            max: 100,
            min: 0,
            padding: {top: 0, bottom: 0}
          }
        },
        bindto: "#chart_neighbors"
      });
}


function getValidValue(value) {
    if(value == -1)
        value = 0
    return value
}

function findNeighbors(result) {
    var len = result.length
    var pos = 0
    for (var i=0; i < len; i++) {
        if(result[i].vara_id == vara_id) {
            pos = i
            break
        }
    }   
    
    var left = pos
    var right = len - pos - 1

    if(left >= 2) {
        if(right == 0) {
            if(left >= 4)
                return result.slice(pos-4, pos+1)
            else if(left >= 3)
                return result.slice(pos-3, pos+1)
            else if(left >= 2)
                return result.slice(pos-2, pos+1)
            else if (left >= 1)
                return result.slice(pos-1, pos+1)
            else
                return result.slice(pos, pos+1)
        }
        else if(right == 1){
            if(left >= 3)
                return result.slice(pos-3, pos+2)
            else
                return result.slice(pos-2, pos+1)
        }
        else if(right == 2){
            return result.slice(pos-2, pos+3)
        }
    }
    else if(left ==1) {
        if(right >= 3)
            return result.slice(pos-1, pos+4)
        else {
            if(right == 2)
                return result.slice(pos-1, pos+3)
            else if (right == 1)
                return result.slice(pos-1, pos+2)
            else
                return result.slice(pos-1, pos+1)
        }
    }
    else {
        if(right >= 4)
            return result.slice(pos-1, pos+5)
        else if(right == 3) 
            return result.slice(pos-1, pos+4)
        else if(right == 2)
            return result.slice(pos-1, pos+3)
        else if (right == 1)
            return result.slice(pos-1, pos+2)
        else
            return result.slice(pos, pos+1)
        
    }
}