cmake_minimum_required(VERSION 3.10)

project(MeuProjeto LANGUAGES C)

set(CMAKE_C_FLAGS_DEBUG  "${CMAKE_C_FLAGS_DEBUG} -g -O0")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0")

# Pega todos os arquivos .c da pasta src/
file(GLOB SRC_FILES src_c/*.c)

# Cria o executável
add_executable(meu_projeto ${SRC_FILES})
