#!/bin/bash
wsk action delete sequence_scrap || true
wsk action delete sequence_web || true

wsk action create sequence_scrap --sequence metacritic,rawg
wsk action create sequence_web --sequence metacritic,rawg,render_web --web true