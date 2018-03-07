--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: event; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE event (
    eventid character varying NOT NULL,
    eventname character varying,
    roomid character varying,
    starttime numeric,
    endtime numeric,
    bookpeople character varying
);


ALTER TABLE public.event OWNER TO postgres;

--
-- Name: room; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE room (
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

COPY event (eventid, eventname, roomid, starttime, endtime, bookpeople) FROM stdin;
\.


--
-- Data for Name: room; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY room (roomid, roomname, building, floor, maxpeople) FROM stdin;
suzhouhe.pwc@gmail.com	suzhouhe	A 	7	10
dashijie.pwc@gmail.com	suzhouhe	A 	11	8
renminguangchang.pwc@gmail.com	renminguangchang	B 	6	12
\.


--
-- Name: event_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY event
    ADD CONSTRAINT event_pkey PRIMARY KEY (eventid);


--
-- Name: room_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY room
    ADD CONSTRAINT room_pkey PRIMARY KEY (roomid);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

