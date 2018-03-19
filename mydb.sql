--
-- PostgreSQL database dump
--

-- Dumped from database version 10.3
-- Dumped by pg_dump version 10.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: event; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.event (
    eventid character varying NOT NULL,
    eventname character varying,
    roomid character varying,
    starttime numeric,
    endtime numeric,
    bookpeople character varying
);


ALTER TABLE public.event OWNER TO postgres;

--
-- Name: room; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.room (
    roomid character varying NOT NULL,
    roomname character varying,
    building character(2),
    floor integer,
    maxpeople integer
);


ALTER TABLE public.room OWNER TO postgres;

--
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.event (eventid, eventname, roomid, starttime, endtime, bookpeople) FROM stdin;
0tphdj39dk6vbamgbfo3f1d09c	Meeting Invitation	pwcsuzhouhe@gmail.com	1521136800.0	1521144000.0	anna.z.jin@gmail.com
5nrhm709j7kuligf7ulc687m80	Meeting Invitation	pwcsuzhouhe@gmail.com	1521147600.0	1521151200.0	anna.z.jin@gmail.com
\.


--
-- Data for Name: room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.room (roomid, roomname, building, floor, maxpeople) FROM stdin;
pwcsuzhouhe@gmail.com	suzhouhe	A 	7	10
\.


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (eventid);


--
-- Name: room room_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (roomid);


--
-- PostgreSQL database dump complete
--

