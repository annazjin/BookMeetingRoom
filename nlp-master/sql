-- Table: public.event

-- DROP TABLE public.event;

CREATE TABLE public.event
(
    eventid bigint NOT NULL,
    eventname character varying COLLATE pg_catalog."default",
    roomid integer,
    starttime numeric,
    endtime numeric,
    bookpeople character varying COLLATE pg_catalog."default",
    CONSTRAINT event_pkey PRIMARY KEY (eventid)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.event
    OWNER to postgres;





-- Table: public.room

-- DROP TABLE public.room;

CREATE TABLE public.room
(
    roomid integer NOT NULL,
    roomname character varying COLLATE pg_catalog."default",
    building character(2) COLLATE pg_catalog."default",
    floor integer,
    maxpeople integer,
    CONSTRAINT room_pkey PRIMARY KEY (roomid)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.room
    OWNER to postgres;
