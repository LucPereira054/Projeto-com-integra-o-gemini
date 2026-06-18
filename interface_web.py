import streamlit as st
from lista_tarefas import adcionar_tarefas, listar_tarefas, marcar_concluida, otimizar_com_ai

st.title("Minha lista de Tarefas")

nova_tarefa=st.text_input("Digite uma nova tarefa: ")
if st.button("Adcionar"):
    adcionar_tarefas(nova_tarefa)
    st.success("Tarefa adcionada")


if 'tarefas' not in st.session_state:
    st.session_state.tarefas=listar_tarefas()

tarefas=st.session_state.tarefas

st.subheader("Suas tarefas: ")
if not tarefas:
    st.write("Nenhuma tarefa na lista neste momento.")
else:
    for index,t in enumerate(tarefas,start=1):
        status="feito" if t['status']=='concluída' else" ainda não feita."
        st.write(f"{index}. {t['descricao']} - {status}")

st.divider()

st.subheader("Assitente de Pordutividade!!!")
st.write("Deixe a IA sugerir a melhor ordem para você excutar suas tarefas de hoje e até mesmo sugerir o que você pode fazer!")

if st.button("Otimizar com a AI"):
    if not tarefas:
        st.warning("Adicione algumas tarefas para que eu possa lhe ajudar!")
    else:
        with st.spinner("Analisando seu dia..."):
            sugestao=otimizar_com_ai(tarefas)
    st.success("Aqui está uma sugestão para otimizar a sua rotina.")
    st.info(sugestao)


st.divider()

st.subheader("Concluir as tarefas!!")

max_val=len(tarefas) if len(tarefas)> 0 else 1

idx_para_concluir=st.number_input("Número da tarefa para marcar como concluida:"
                                  ,min_value=1,max_value=max_val,step=1)

if st.button("Marcar como concluida"):
    if not tarefas:
        st.warning("Não há tarefas para concluir.")
    elif marcar_concluida(idx_para_concluir):
        st.session_state.tarefas=listar_tarefas()
        st.success("tarefa atualizada com sucesso!")
        st.rerun()
    else:
        st.error("ìndice inválido ou erro ao concluir.")

