--
-- PostgreSQL database dump
--

-- Dumped from database version 11.1
-- Dumped by pg_dump version 11.2

-- Started on 2019-04-18 19:52:20

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
-- TOC entry 2 (class 3079 OID 16397)
-- Name: pg_trgm; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;


--
-- TOC entry 2805 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION pg_trgm; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_trgm IS 'text similarity measurement and index searching based on trigrams';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 262 (class 1259 OID 4991030)
-- Name: db_poe_account; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_account (
    poe_account_uuid uuid NOT NULL,
    poe_account_name text,
    poe_account_value numeric,
    poe_account_characters jsonb
);


ALTER TABLE public.db_poe_account OWNER TO postgres;

--
-- TOC entry 264 (class 1259 OID 4996209)
-- Name: db_poe_account_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_account_items (
    db_poe_account_item_uuid text NOT NULL,
    db_poe_account_uuid uuid,
    db_poe_account_item_class_uuid uuid,
    db_poe_account_item_json jsonb
);


ALTER TABLE public.db_poe_account_items OWNER TO postgres;

--
-- TOC entry 263 (class 1259 OID 4991039)
-- Name: db_poe_character; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_character (
    db_poe_character_uuid uuid NOT NULL,
    db_poe_account_uuid uuid,
    db_poe_character_name text,
    db_poe_character_json jsonb,
    db_poe_character_passive_json jsonb,
    db_poe_character_items_json jsonb
);


ALTER TABLE public.db_poe_character OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 4978144)
-- Name: db_poe_chat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_chat (
    chat_uuid uuid NOT NULL,
    chat_text text,
    chat_type smallint,
    chat_timestamp timestamp without time zone,
    chat_user text
);


ALTER TABLE public.db_poe_chat OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 4976342)
-- Name: db_poe_essence_base; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_essence_base (
    db_poe_essence_uuid uuid NOT NULL,
    db_poe_essance_name text,
    db_poe_essence_json jsonb
);


ALTER TABLE public.db_poe_essence_base OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 4976353)
-- Name: db_poe_gem_base; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_gem_base (
    db_poe_gem_uuid uuid NOT NULL,
    db_poe_gem_name text,
    db_poe_gem_json jsonb
);


ALTER TABLE public.db_poe_gem_base OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 4976266)
-- Name: db_poe_item_class; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_item_class (
    item_class_uuid uuid NOT NULL,
    db_poe_item_class_name text,
    db_poe_item_class_json jsonb
);


ALTER TABLE public.db_poe_item_class OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 4976298)
-- Name: db_poe_item_subtypes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_item_subtypes (
    item_subtype_uuid uuid NOT NULL,
    db_poe_item_subtype_name text,
    db_poe_item_subtype_json jsonb,
    db_poe_item_subtype_class_uuid uuid
);


ALTER TABLE public.db_poe_item_subtypes OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 4978134)
-- Name: db_poe_league; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_league (
    league_uuid uuid NOT NULL,
    league_name text,
    league_json jsonb
);


ALTER TABLE public.db_poe_league OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 4987553)
-- Name: db_poe_market_abyssjewel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_abyssjewel (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_abyssjewel OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 4987567)
-- Name: db_poe_market_active_skill_gem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_active_skill_gem (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_active_skill_gem OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 4987581)
-- Name: db_poe_market_amulet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_amulet (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_amulet OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 4987595)
-- Name: db_poe_market_belt; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_belt (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_belt OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 4987609)
-- Name: db_poe_market_body_armour; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_body_armour (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_body_armour OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 4987623)
-- Name: db_poe_market_boots; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_boots (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_boots OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 4987637)
-- Name: db_poe_market_bow; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_bow (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_bow OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 4987651)
-- Name: db_poe_market_claw; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_claw (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_claw OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 4987665)
-- Name: db_poe_market_currency; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_currency (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_currency OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 4987679)
-- Name: db_poe_market_dagger; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_dagger (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_dagger OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 4987693)
-- Name: db_poe_market_delvesocketablecurrency; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_delvesocketablecurrency (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_delvesocketablecurrency OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 4987707)
-- Name: db_poe_market_divinationcard; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_divinationcard (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_divinationcard OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 4987721)
-- Name: db_poe_market_fishingrod; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_fishingrod (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_fishingrod OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 4987735)
-- Name: db_poe_market_gloves; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_gloves (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_gloves OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 4987749)
-- Name: db_poe_market_helmet; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_helmet (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_helmet OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 4987763)
-- Name: db_poe_market_hideoutdoodad; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_hideoutdoodad (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_hideoutdoodad OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 4987777)
-- Name: db_poe_market_hybridflask; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_hybridflask (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_hybridflask OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 4987791)
-- Name: db_poe_market_incursionitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_incursionitem (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_incursionitem OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 4987805)
-- Name: db_poe_market_jewel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_jewel (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_jewel OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 4987819)
-- Name: db_poe_market_labyrinthitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_labyrinthitem (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_labyrinthitem OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 4987833)
-- Name: db_poe_market_labyrinthmapitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_labyrinthmapitem (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_labyrinthmapitem OWNER TO postgres;

--
-- TOC entry 230 (class 1259 OID 4987847)
-- Name: db_poe_market_labyrinthtrinket; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_labyrinthtrinket (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_labyrinthtrinket OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 4987861)
-- Name: db_poe_market_largerelic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_largerelic (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_largerelic OWNER TO postgres;

--
-- TOC entry 232 (class 1259 OID 4987875)
-- Name: db_poe_market_leaguestone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_leaguestone (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_leaguestone OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 4987889)
-- Name: db_poe_market_lifeflask; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_lifeflask (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_lifeflask OWNER TO postgres;

--
-- TOC entry 234 (class 1259 OID 4987903)
-- Name: db_poe_market_manaflask; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_manaflask (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_manaflask OWNER TO postgres;

--
-- TOC entry 235 (class 1259 OID 4987917)
-- Name: db_poe_market_map; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_map (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_map OWNER TO postgres;

--
-- TOC entry 236 (class 1259 OID 4987931)
-- Name: db_poe_market_mapfragment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_mapfragment (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_mapfragment OWNER TO postgres;

--
-- TOC entry 237 (class 1259 OID 4987945)
-- Name: db_poe_market_mediumrelic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_mediumrelic (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_mediumrelic OWNER TO postgres;

--
-- TOC entry 238 (class 1259 OID 4987959)
-- Name: db_poe_market_microtransaction; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_microtransaction (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_microtransaction OWNER TO postgres;

--
-- TOC entry 239 (class 1259 OID 4987973)
-- Name: db_poe_market_miscmapitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_miscmapitem (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_miscmapitem OWNER TO postgres;

--
-- TOC entry 240 (class 1259 OID 4987987)
-- Name: db_poe_market_one_hand_axe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_one_hand_axe (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_one_hand_axe OWNER TO postgres;

--
-- TOC entry 241 (class 1259 OID 4988001)
-- Name: db_poe_market_one_hand_mace; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_one_hand_mace (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_one_hand_mace OWNER TO postgres;

--
-- TOC entry 242 (class 1259 OID 4988015)
-- Name: db_poe_market_one_hand_sword; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_one_hand_sword (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_one_hand_sword OWNER TO postgres;

--
-- TOC entry 243 (class 1259 OID 4988029)
-- Name: db_poe_market_pantheonsoul; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_pantheonsoul (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_pantheonsoul OWNER TO postgres;

--
-- TOC entry 244 (class 1259 OID 4988043)
-- Name: db_poe_market_questitem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_questitem (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_questitem OWNER TO postgres;

--
-- TOC entry 245 (class 1259 OID 4988057)
-- Name: db_poe_market_quiver; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_quiver (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_quiver OWNER TO postgres;

--
-- TOC entry 246 (class 1259 OID 4988071)
-- Name: db_poe_market_ring; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_ring (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_ring OWNER TO postgres;

--
-- TOC entry 247 (class 1259 OID 4988085)
-- Name: db_poe_market_sceptre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_sceptre (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_sceptre OWNER TO postgres;

--
-- TOC entry 248 (class 1259 OID 4988099)
-- Name: db_poe_market_shield; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_shield (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_shield OWNER TO postgres;

--
-- TOC entry 249 (class 1259 OID 4988113)
-- Name: db_poe_market_smallrelic; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_smallrelic (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_smallrelic OWNER TO postgres;

--
-- TOC entry 250 (class 1259 OID 4988127)
-- Name: db_poe_market_stackablecurrency; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_stackablecurrency (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_stackablecurrency OWNER TO postgres;

--
-- TOC entry 251 (class 1259 OID 4988141)
-- Name: db_poe_market_staff; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_staff (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_staff OWNER TO postgres;

--
-- TOC entry 252 (class 1259 OID 4988155)
-- Name: db_poe_market_support_skill_gem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_support_skill_gem (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_support_skill_gem OWNER TO postgres;

--
-- TOC entry 253 (class 1259 OID 4988169)
-- Name: db_poe_market_thrusting_one_hand_sword; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_thrusting_one_hand_sword (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_thrusting_one_hand_sword OWNER TO postgres;

--
-- TOC entry 254 (class 1259 OID 4988183)
-- Name: db_poe_market_two_hand_axe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_two_hand_axe (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_two_hand_axe OWNER TO postgres;

--
-- TOC entry 255 (class 1259 OID 4988197)
-- Name: db_poe_market_two_hand_mace; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_two_hand_mace (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_two_hand_mace OWNER TO postgres;

--
-- TOC entry 256 (class 1259 OID 4988211)
-- Name: db_poe_market_two_hand_sword; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_two_hand_sword (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_two_hand_sword OWNER TO postgres;

--
-- TOC entry 257 (class 1259 OID 4988225)
-- Name: db_poe_market_unarmed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_unarmed (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_unarmed OWNER TO postgres;

--
-- TOC entry 258 (class 1259 OID 4988239)
-- Name: db_poe_market_uniquefragment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_uniquefragment (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_uniquefragment OWNER TO postgres;

--
-- TOC entry 259 (class 1259 OID 4988253)
-- Name: db_poe_market_utilityflask; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_utilityflask (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_utilityflask OWNER TO postgres;

--
-- TOC entry 260 (class 1259 OID 4988267)
-- Name: db_poe_market_utilityflaskcritical; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_utilityflaskcritical (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_utilityflaskcritical OWNER TO postgres;

--
-- TOC entry 261 (class 1259 OID 4988281)
-- Name: db_poe_market_wand; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_market_wand (
    market_item_uuid uuid NOT NULL,
    market_item_stash_uuid uuid,
    market_item_json jsonb
);


ALTER TABLE public.db_poe_market_wand OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 4976574)
-- Name: db_poe_mod_base; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_mod_base (
    db_poe_mod_uuid uuid NOT NULL,
    db_poe_mod_name text,
    db_poe_mod_json jsonb
);


ALTER TABLE public.db_poe_mod_base OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 4976330)
-- Name: db_poe_monster_base; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_monster_base (
    db_poe_monster_uuid uuid NOT NULL,
    db_poe_monster_level text,
    db_poe_monster_json jsonb
);


ALTER TABLE public.db_poe_monster_base OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16486)
-- Name: db_poe_stashes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_stashes (
    poe_stash_uuid uuid NOT NULL,
    poe_stash_account_uuid uuid,
    poe_stash_json_data jsonb,
    poe_stash_id_uuid text,
    poe_league_uuid uuid
);


ALTER TABLE public.db_poe_stashes OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 4977427)
-- Name: db_poe_stat_base; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_stat_base (
    db_poe_stat_uuid uuid NOT NULL,
    db_poe_stat_name text,
    db_poe_stat_json jsonb
);


ALTER TABLE public.db_poe_stat_base OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 16614)
-- Name: db_poe_status; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_poe_status (
    poe_status_change_id text NOT NULL
);


ALTER TABLE public.db_poe_status OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 16391)
-- Name: db_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.db_user (
    id integer NOT NULL,
    username text,
    email text,
    password text,
    created_at timestamp with time zone,
    active boolean,
    is_admin boolean,
    user_json jsonb,
    lang text
);


ALTER TABLE public.db_user OWNER TO postgres;

--
-- TOC entry 2615 (class 2606 OID 4991037)
-- Name: db_poe_account account_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_account
    ADD CONSTRAINT account_uuid_pk PRIMARY KEY (poe_account_uuid);


--
-- TOC entry 2451 (class 2606 OID 4978151)
-- Name: db_poe_chat chat_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_chat
    ADD CONSTRAINT chat_uuid_pk PRIMARY KEY (chat_uuid);


--
-- TOC entry 2621 (class 2606 OID 4996216)
-- Name: db_poe_account_items db_poe_account_item_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_account_items
    ADD CONSTRAINT db_poe_account_item_uuid_pk PRIMARY KEY (db_poe_account_item_uuid);


--
-- TOC entry 2619 (class 2606 OID 4991046)
-- Name: db_poe_character db_poe_character_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_character
    ADD CONSTRAINT db_poe_character_uuid_pk PRIMARY KEY (db_poe_character_uuid);


--
-- TOC entry 2437 (class 2606 OID 4976349)
-- Name: db_poe_essence_base db_poe_essence_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_essence_base
    ADD CONSTRAINT db_poe_essence_uuid_pk PRIMARY KEY (db_poe_essence_uuid);


--
-- TOC entry 2440 (class 2606 OID 4976360)
-- Name: db_poe_gem_base db_poe_gem_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_gem_base
    ADD CONSTRAINT db_poe_gem_uuid_pk PRIMARY KEY (db_poe_gem_uuid);


--
-- TOC entry 2443 (class 2606 OID 4976581)
-- Name: db_poe_mod_base db_poe_mod_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_mod_base
    ADD CONSTRAINT db_poe_mod_uuid_pk PRIMARY KEY (db_poe_mod_uuid);


--
-- TOC entry 2434 (class 2606 OID 4976337)
-- Name: db_poe_monster_base db_poe_monster_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_monster_base
    ADD CONSTRAINT db_poe_monster_uuid_pk PRIMARY KEY (db_poe_monster_uuid);


--
-- TOC entry 2446 (class 2606 OID 4977434)
-- Name: db_poe_stat_base db_poe_stat_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_stat_base
    ADD CONSTRAINT db_poe_stat_uuid_pk PRIMARY KEY (db_poe_stat_uuid);


--
-- TOC entry 2427 (class 2606 OID 4976273)
-- Name: db_poe_item_class item_class_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_item_class
    ADD CONSTRAINT item_class_uuid_pk PRIMARY KEY (item_class_uuid);


--
-- TOC entry 2431 (class 2606 OID 4976305)
-- Name: db_poe_item_subtypes item_subtype_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_item_subtypes
    ADD CONSTRAINT item_subtype_uuid_pk PRIMARY KEY (item_subtype_uuid);


--
-- TOC entry 2449 (class 2606 OID 4978141)
-- Name: db_poe_league league_uuid_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_league
    ADD CONSTRAINT league_uuid_pk PRIMARY KEY (league_uuid);


--
-- TOC entry 2457 (class 2606 OID 4987560)
-- Name: db_poe_market_abyssjewel market_item_uuid_abyssjewel_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_abyssjewel
    ADD CONSTRAINT market_item_uuid_abyssjewel_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2460 (class 2606 OID 4987574)
-- Name: db_poe_market_active_skill_gem market_item_uuid_active_skill_gem_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_active_skill_gem
    ADD CONSTRAINT market_item_uuid_active_skill_gem_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2463 (class 2606 OID 4987588)
-- Name: db_poe_market_amulet market_item_uuid_amulet_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_amulet
    ADD CONSTRAINT market_item_uuid_amulet_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2466 (class 2606 OID 4987602)
-- Name: db_poe_market_belt market_item_uuid_belt_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_belt
    ADD CONSTRAINT market_item_uuid_belt_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2469 (class 2606 OID 4987616)
-- Name: db_poe_market_body_armour market_item_uuid_body_armour_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_body_armour
    ADD CONSTRAINT market_item_uuid_body_armour_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2472 (class 2606 OID 4987630)
-- Name: db_poe_market_boots market_item_uuid_boots_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_boots
    ADD CONSTRAINT market_item_uuid_boots_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2475 (class 2606 OID 4987644)
-- Name: db_poe_market_bow market_item_uuid_bow_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_bow
    ADD CONSTRAINT market_item_uuid_bow_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2478 (class 2606 OID 4987658)
-- Name: db_poe_market_claw market_item_uuid_claw_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_claw
    ADD CONSTRAINT market_item_uuid_claw_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2481 (class 2606 OID 4987672)
-- Name: db_poe_market_currency market_item_uuid_currency_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_currency
    ADD CONSTRAINT market_item_uuid_currency_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2484 (class 2606 OID 4987686)
-- Name: db_poe_market_dagger market_item_uuid_dagger_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_dagger
    ADD CONSTRAINT market_item_uuid_dagger_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2487 (class 2606 OID 4987700)
-- Name: db_poe_market_delvesocketablecurrency market_item_uuid_delvesocketablecurrency_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_delvesocketablecurrency
    ADD CONSTRAINT market_item_uuid_delvesocketablecurrency_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2490 (class 2606 OID 4987714)
-- Name: db_poe_market_divinationcard market_item_uuid_divinationcard_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_divinationcard
    ADD CONSTRAINT market_item_uuid_divinationcard_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2493 (class 2606 OID 4987728)
-- Name: db_poe_market_fishingrod market_item_uuid_fishingrod_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_fishingrod
    ADD CONSTRAINT market_item_uuid_fishingrod_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2496 (class 2606 OID 4987742)
-- Name: db_poe_market_gloves market_item_uuid_gloves_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_gloves
    ADD CONSTRAINT market_item_uuid_gloves_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2499 (class 2606 OID 4987756)
-- Name: db_poe_market_helmet market_item_uuid_helmet_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_helmet
    ADD CONSTRAINT market_item_uuid_helmet_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2502 (class 2606 OID 4987770)
-- Name: db_poe_market_hideoutdoodad market_item_uuid_hideoutdoodad_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_hideoutdoodad
    ADD CONSTRAINT market_item_uuid_hideoutdoodad_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2505 (class 2606 OID 4987784)
-- Name: db_poe_market_hybridflask market_item_uuid_hybridflask_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_hybridflask
    ADD CONSTRAINT market_item_uuid_hybridflask_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2508 (class 2606 OID 4987798)
-- Name: db_poe_market_incursionitem market_item_uuid_incursionitem_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_incursionitem
    ADD CONSTRAINT market_item_uuid_incursionitem_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2511 (class 2606 OID 4987812)
-- Name: db_poe_market_jewel market_item_uuid_jewel_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_jewel
    ADD CONSTRAINT market_item_uuid_jewel_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2514 (class 2606 OID 4987826)
-- Name: db_poe_market_labyrinthitem market_item_uuid_labyrinthitem_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_labyrinthitem
    ADD CONSTRAINT market_item_uuid_labyrinthitem_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2517 (class 2606 OID 4987840)
-- Name: db_poe_market_labyrinthmapitem market_item_uuid_labyrinthmapitem_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_labyrinthmapitem
    ADD CONSTRAINT market_item_uuid_labyrinthmapitem_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2520 (class 2606 OID 4987854)
-- Name: db_poe_market_labyrinthtrinket market_item_uuid_labyrinthtrinket_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_labyrinthtrinket
    ADD CONSTRAINT market_item_uuid_labyrinthtrinket_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2523 (class 2606 OID 4987868)
-- Name: db_poe_market_largerelic market_item_uuid_largerelic_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_largerelic
    ADD CONSTRAINT market_item_uuid_largerelic_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2526 (class 2606 OID 4987882)
-- Name: db_poe_market_leaguestone market_item_uuid_leaguestone_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_leaguestone
    ADD CONSTRAINT market_item_uuid_leaguestone_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2529 (class 2606 OID 4987896)
-- Name: db_poe_market_lifeflask market_item_uuid_lifeflask_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_lifeflask
    ADD CONSTRAINT market_item_uuid_lifeflask_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2532 (class 2606 OID 4987910)
-- Name: db_poe_market_manaflask market_item_uuid_manaflask_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_manaflask
    ADD CONSTRAINT market_item_uuid_manaflask_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2535 (class 2606 OID 4987924)
-- Name: db_poe_market_map market_item_uuid_map_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_map
    ADD CONSTRAINT market_item_uuid_map_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2538 (class 2606 OID 4987938)
-- Name: db_poe_market_mapfragment market_item_uuid_mapfragment_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_mapfragment
    ADD CONSTRAINT market_item_uuid_mapfragment_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2541 (class 2606 OID 4987952)
-- Name: db_poe_market_mediumrelic market_item_uuid_mediumrelic_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_mediumrelic
    ADD CONSTRAINT market_item_uuid_mediumrelic_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2544 (class 2606 OID 4987966)
-- Name: db_poe_market_microtransaction market_item_uuid_microtransaction_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_microtransaction
    ADD CONSTRAINT market_item_uuid_microtransaction_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2547 (class 2606 OID 4987980)
-- Name: db_poe_market_miscmapitem market_item_uuid_miscmapitem_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_miscmapitem
    ADD CONSTRAINT market_item_uuid_miscmapitem_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2550 (class 2606 OID 4987994)
-- Name: db_poe_market_one_hand_axe market_item_uuid_one_hand_axe_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_one_hand_axe
    ADD CONSTRAINT market_item_uuid_one_hand_axe_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2553 (class 2606 OID 4988008)
-- Name: db_poe_market_one_hand_mace market_item_uuid_one_hand_mace_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_one_hand_mace
    ADD CONSTRAINT market_item_uuid_one_hand_mace_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2556 (class 2606 OID 4988022)
-- Name: db_poe_market_one_hand_sword market_item_uuid_one_hand_sword_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_one_hand_sword
    ADD CONSTRAINT market_item_uuid_one_hand_sword_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2559 (class 2606 OID 4988036)
-- Name: db_poe_market_pantheonsoul market_item_uuid_pantheonsoul_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_pantheonsoul
    ADD CONSTRAINT market_item_uuid_pantheonsoul_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2562 (class 2606 OID 4988050)
-- Name: db_poe_market_questitem market_item_uuid_questitem_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_questitem
    ADD CONSTRAINT market_item_uuid_questitem_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2565 (class 2606 OID 4988064)
-- Name: db_poe_market_quiver market_item_uuid_quiver_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_quiver
    ADD CONSTRAINT market_item_uuid_quiver_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2568 (class 2606 OID 4988078)
-- Name: db_poe_market_ring market_item_uuid_ring_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_ring
    ADD CONSTRAINT market_item_uuid_ring_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2571 (class 2606 OID 4988092)
-- Name: db_poe_market_sceptre market_item_uuid_sceptre_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_sceptre
    ADD CONSTRAINT market_item_uuid_sceptre_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2574 (class 2606 OID 4988106)
-- Name: db_poe_market_shield market_item_uuid_shield_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_shield
    ADD CONSTRAINT market_item_uuid_shield_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2577 (class 2606 OID 4988120)
-- Name: db_poe_market_smallrelic market_item_uuid_smallrelic_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_smallrelic
    ADD CONSTRAINT market_item_uuid_smallrelic_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2580 (class 2606 OID 4988134)
-- Name: db_poe_market_stackablecurrency market_item_uuid_stackablecurrency_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_stackablecurrency
    ADD CONSTRAINT market_item_uuid_stackablecurrency_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2583 (class 2606 OID 4988148)
-- Name: db_poe_market_staff market_item_uuid_staff_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_staff
    ADD CONSTRAINT market_item_uuid_staff_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2586 (class 2606 OID 4988162)
-- Name: db_poe_market_support_skill_gem market_item_uuid_support_skill_gem_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_support_skill_gem
    ADD CONSTRAINT market_item_uuid_support_skill_gem_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2589 (class 2606 OID 4988176)
-- Name: db_poe_market_thrusting_one_hand_sword market_item_uuid_thrusting_one_hand_sword_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_thrusting_one_hand_sword
    ADD CONSTRAINT market_item_uuid_thrusting_one_hand_sword_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2592 (class 2606 OID 4988190)
-- Name: db_poe_market_two_hand_axe market_item_uuid_two_hand_axe_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_two_hand_axe
    ADD CONSTRAINT market_item_uuid_two_hand_axe_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2595 (class 2606 OID 4988204)
-- Name: db_poe_market_two_hand_mace market_item_uuid_two_hand_mace_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_two_hand_mace
    ADD CONSTRAINT market_item_uuid_two_hand_mace_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2598 (class 2606 OID 4988218)
-- Name: db_poe_market_two_hand_sword market_item_uuid_two_hand_sword_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_two_hand_sword
    ADD CONSTRAINT market_item_uuid_two_hand_sword_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2601 (class 2606 OID 4988232)
-- Name: db_poe_market_unarmed market_item_uuid_unarmed_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_unarmed
    ADD CONSTRAINT market_item_uuid_unarmed_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2604 (class 2606 OID 4988246)
-- Name: db_poe_market_uniquefragment market_item_uuid_uniquefragment_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_uniquefragment
    ADD CONSTRAINT market_item_uuid_uniquefragment_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2607 (class 2606 OID 4988260)
-- Name: db_poe_market_utilityflask market_item_uuid_utilityflask_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_utilityflask
    ADD CONSTRAINT market_item_uuid_utilityflask_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2610 (class 2606 OID 4988274)
-- Name: db_poe_market_utilityflaskcritical market_item_uuid_utilityflaskcritical_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_utilityflaskcritical
    ADD CONSTRAINT market_item_uuid_utilityflaskcritical_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2612 (class 2606 OID 4988288)
-- Name: db_poe_market_wand market_item_uuid_wand_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_wand
    ADD CONSTRAINT market_item_uuid_wand_pk PRIMARY KEY (market_item_uuid);


--
-- TOC entry 2617 (class 1259 OID 4991052)
-- Name: db_poe_character_name_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX db_poe_character_name_ndx ON public.db_poe_character USING btree (db_poe_character_name);


--
-- TOC entry 2452 (class 1259 OID 4978153)
-- Name: db_poe_chat_timestamp_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX db_poe_chat_timestamp_ndx ON public.db_poe_chat USING btree (chat_timestamp);


--
-- TOC entry 2453 (class 1259 OID 4978152)
-- Name: db_poe_chat_type_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX db_poe_chat_type_ndx ON public.db_poe_chat USING btree (chat_type);


--
-- TOC entry 2454 (class 1259 OID 4978154)
-- Name: db_poe_chat_user_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX db_poe_chat_user_ndx ON public.db_poe_chat USING btree (chat_user);


--
-- TOC entry 2435 (class 1259 OID 4976350)
-- Name: db_poe_essance_name_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX db_poe_essance_name_ndx ON public.db_poe_essence_base USING btree (db_poe_essance_name);


--
-- TOC entry 2438 (class 1259 OID 4976361)
-- Name: db_poe_gem_name_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX db_poe_gem_name_ndx ON public.db_poe_gem_base USING btree (db_poe_gem_name);


--
-- TOC entry 2425 (class 1259 OID 4976274)
-- Name: db_poe_item_class_name_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX db_poe_item_class_name_ndx ON public.db_poe_item_class USING btree (db_poe_item_class_name);


--
-- TOC entry 2428 (class 1259 OID 4976312)
-- Name: db_poe_item_subtype_class_uuid_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX db_poe_item_subtype_class_uuid_ndx ON public.db_poe_item_subtypes USING btree (db_poe_item_subtype_class_uuid);


--
-- TOC entry 2429 (class 1259 OID 4976311)
-- Name: db_poe_item_subtype_name_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX db_poe_item_subtype_name_ndx ON public.db_poe_item_subtypes USING btree (db_poe_item_subtype_name);


--
-- TOC entry 2447 (class 1259 OID 4978142)
-- Name: db_poe_league_name_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX db_poe_league_name_ndx ON public.db_poe_league USING btree (league_name);


--
-- TOC entry 2441 (class 1259 OID 4976582)
-- Name: db_poe_mod_name_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX db_poe_mod_name_ndx ON public.db_poe_mod_base USING btree (db_poe_mod_name);


--
-- TOC entry 2432 (class 1259 OID 4976338)
-- Name: db_poe_monster_level_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX db_poe_monster_level_ndx ON public.db_poe_monster_base USING btree (db_poe_monster_level);


--
-- TOC entry 2444 (class 1259 OID 4977435)
-- Name: db_poe_stat_name_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX db_poe_stat_name_ndx ON public.db_poe_stat_base USING btree (db_poe_stat_name);


--
-- TOC entry 2455 (class 1259 OID 4987566)
-- Name: market_item_abyssjewel_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_abyssjewel_stash_ndx ON public.db_poe_market_abyssjewel USING btree (market_item_stash_uuid);


--
-- TOC entry 2458 (class 1259 OID 4987580)
-- Name: market_item_active_skill_gem_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_active_skill_gem_stash_ndx ON public.db_poe_market_active_skill_gem USING btree (market_item_stash_uuid);


--
-- TOC entry 2461 (class 1259 OID 4987594)
-- Name: market_item_amulet_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_amulet_stash_ndx ON public.db_poe_market_amulet USING btree (market_item_stash_uuid);


--
-- TOC entry 2464 (class 1259 OID 4987608)
-- Name: market_item_belt_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_belt_stash_ndx ON public.db_poe_market_belt USING btree (market_item_stash_uuid);


--
-- TOC entry 2467 (class 1259 OID 4987622)
-- Name: market_item_body_armour_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_body_armour_stash_ndx ON public.db_poe_market_body_armour USING btree (market_item_stash_uuid);


--
-- TOC entry 2470 (class 1259 OID 4987636)
-- Name: market_item_boots_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_boots_stash_ndx ON public.db_poe_market_boots USING btree (market_item_stash_uuid);


--
-- TOC entry 2473 (class 1259 OID 4987650)
-- Name: market_item_bow_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_bow_stash_ndx ON public.db_poe_market_bow USING btree (market_item_stash_uuid);


--
-- TOC entry 2476 (class 1259 OID 4987664)
-- Name: market_item_claw_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_claw_stash_ndx ON public.db_poe_market_claw USING btree (market_item_stash_uuid);


--
-- TOC entry 2479 (class 1259 OID 4987678)
-- Name: market_item_currency_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_currency_stash_ndx ON public.db_poe_market_currency USING btree (market_item_stash_uuid);


--
-- TOC entry 2482 (class 1259 OID 4987692)
-- Name: market_item_dagger_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_dagger_stash_ndx ON public.db_poe_market_dagger USING btree (market_item_stash_uuid);


--
-- TOC entry 2485 (class 1259 OID 4987706)
-- Name: market_item_delvesocketablecurrency_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_delvesocketablecurrency_stash_ndx ON public.db_poe_market_delvesocketablecurrency USING btree (market_item_stash_uuid);


--
-- TOC entry 2488 (class 1259 OID 4987720)
-- Name: market_item_divinationcard_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_divinationcard_stash_ndx ON public.db_poe_market_divinationcard USING btree (market_item_stash_uuid);


--
-- TOC entry 2491 (class 1259 OID 4987734)
-- Name: market_item_fishingrod_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_fishingrod_stash_ndx ON public.db_poe_market_fishingrod USING btree (market_item_stash_uuid);


--
-- TOC entry 2494 (class 1259 OID 4987748)
-- Name: market_item_gloves_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_gloves_stash_ndx ON public.db_poe_market_gloves USING btree (market_item_stash_uuid);


--
-- TOC entry 2497 (class 1259 OID 4987762)
-- Name: market_item_helmet_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_helmet_stash_ndx ON public.db_poe_market_helmet USING btree (market_item_stash_uuid);


--
-- TOC entry 2500 (class 1259 OID 4987776)
-- Name: market_item_hideoutdoodad_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_hideoutdoodad_stash_ndx ON public.db_poe_market_hideoutdoodad USING btree (market_item_stash_uuid);


--
-- TOC entry 2503 (class 1259 OID 4987790)
-- Name: market_item_hybridflask_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_hybridflask_stash_ndx ON public.db_poe_market_hybridflask USING btree (market_item_stash_uuid);


--
-- TOC entry 2506 (class 1259 OID 4987804)
-- Name: market_item_incursionitem_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_incursionitem_stash_ndx ON public.db_poe_market_incursionitem USING btree (market_item_stash_uuid);


--
-- TOC entry 2509 (class 1259 OID 4987818)
-- Name: market_item_jewel_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_jewel_stash_ndx ON public.db_poe_market_jewel USING btree (market_item_stash_uuid);


--
-- TOC entry 2512 (class 1259 OID 4987832)
-- Name: market_item_labyrinthitem_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_labyrinthitem_stash_ndx ON public.db_poe_market_labyrinthitem USING btree (market_item_stash_uuid);


--
-- TOC entry 2515 (class 1259 OID 4987846)
-- Name: market_item_labyrinthmapitem_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_labyrinthmapitem_stash_ndx ON public.db_poe_market_labyrinthmapitem USING btree (market_item_stash_uuid);


--
-- TOC entry 2518 (class 1259 OID 4987860)
-- Name: market_item_labyrinthtrinket_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_labyrinthtrinket_stash_ndx ON public.db_poe_market_labyrinthtrinket USING btree (market_item_stash_uuid);


--
-- TOC entry 2521 (class 1259 OID 4987874)
-- Name: market_item_largerelic_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_largerelic_stash_ndx ON public.db_poe_market_largerelic USING btree (market_item_stash_uuid);


--
-- TOC entry 2524 (class 1259 OID 4987888)
-- Name: market_item_leaguestone_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_leaguestone_stash_ndx ON public.db_poe_market_leaguestone USING btree (market_item_stash_uuid);


--
-- TOC entry 2527 (class 1259 OID 4987902)
-- Name: market_item_lifeflask_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_lifeflask_stash_ndx ON public.db_poe_market_lifeflask USING btree (market_item_stash_uuid);


--
-- TOC entry 2530 (class 1259 OID 4987916)
-- Name: market_item_manaflask_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_manaflask_stash_ndx ON public.db_poe_market_manaflask USING btree (market_item_stash_uuid);


--
-- TOC entry 2533 (class 1259 OID 4987930)
-- Name: market_item_map_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_map_stash_ndx ON public.db_poe_market_map USING btree (market_item_stash_uuid);


--
-- TOC entry 2536 (class 1259 OID 4987944)
-- Name: market_item_mapfragment_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_mapfragment_stash_ndx ON public.db_poe_market_mapfragment USING btree (market_item_stash_uuid);


--
-- TOC entry 2539 (class 1259 OID 4987958)
-- Name: market_item_mediumrelic_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_mediumrelic_stash_ndx ON public.db_poe_market_mediumrelic USING btree (market_item_stash_uuid);


--
-- TOC entry 2542 (class 1259 OID 4987972)
-- Name: market_item_microtransaction_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_microtransaction_stash_ndx ON public.db_poe_market_microtransaction USING btree (market_item_stash_uuid);


--
-- TOC entry 2545 (class 1259 OID 4987986)
-- Name: market_item_miscmapitem_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_miscmapitem_stash_ndx ON public.db_poe_market_miscmapitem USING btree (market_item_stash_uuid);


--
-- TOC entry 2548 (class 1259 OID 4988000)
-- Name: market_item_one_hand_axe_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_one_hand_axe_stash_ndx ON public.db_poe_market_one_hand_axe USING btree (market_item_stash_uuid);


--
-- TOC entry 2551 (class 1259 OID 4988014)
-- Name: market_item_one_hand_mace_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_one_hand_mace_stash_ndx ON public.db_poe_market_one_hand_mace USING btree (market_item_stash_uuid);


--
-- TOC entry 2554 (class 1259 OID 4988028)
-- Name: market_item_one_hand_sword_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_one_hand_sword_stash_ndx ON public.db_poe_market_one_hand_sword USING btree (market_item_stash_uuid);


--
-- TOC entry 2557 (class 1259 OID 4988042)
-- Name: market_item_pantheonsoul_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_pantheonsoul_stash_ndx ON public.db_poe_market_pantheonsoul USING btree (market_item_stash_uuid);


--
-- TOC entry 2560 (class 1259 OID 4988056)
-- Name: market_item_questitem_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_questitem_stash_ndx ON public.db_poe_market_questitem USING btree (market_item_stash_uuid);


--
-- TOC entry 2563 (class 1259 OID 4988070)
-- Name: market_item_quiver_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_quiver_stash_ndx ON public.db_poe_market_quiver USING btree (market_item_stash_uuid);


--
-- TOC entry 2566 (class 1259 OID 4988084)
-- Name: market_item_ring_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_ring_stash_ndx ON public.db_poe_market_ring USING btree (market_item_stash_uuid);


--
-- TOC entry 2569 (class 1259 OID 4988098)
-- Name: market_item_sceptre_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_sceptre_stash_ndx ON public.db_poe_market_sceptre USING btree (market_item_stash_uuid);


--
-- TOC entry 2572 (class 1259 OID 4988112)
-- Name: market_item_shield_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_shield_stash_ndx ON public.db_poe_market_shield USING btree (market_item_stash_uuid);


--
-- TOC entry 2575 (class 1259 OID 4988126)
-- Name: market_item_smallrelic_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_smallrelic_stash_ndx ON public.db_poe_market_smallrelic USING btree (market_item_stash_uuid);


--
-- TOC entry 2578 (class 1259 OID 4988140)
-- Name: market_item_stackablecurrency_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_stackablecurrency_stash_ndx ON public.db_poe_market_stackablecurrency USING btree (market_item_stash_uuid);


--
-- TOC entry 2581 (class 1259 OID 4988154)
-- Name: market_item_staff_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_staff_stash_ndx ON public.db_poe_market_staff USING btree (market_item_stash_uuid);


--
-- TOC entry 2584 (class 1259 OID 4988168)
-- Name: market_item_support_skill_gem_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_support_skill_gem_stash_ndx ON public.db_poe_market_support_skill_gem USING btree (market_item_stash_uuid);


--
-- TOC entry 2587 (class 1259 OID 4988182)
-- Name: market_item_thrusting_one_hand_sword_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_thrusting_one_hand_sword_stash_ndx ON public.db_poe_market_thrusting_one_hand_sword USING btree (market_item_stash_uuid);


--
-- TOC entry 2590 (class 1259 OID 4988196)
-- Name: market_item_two_hand_axe_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_two_hand_axe_stash_ndx ON public.db_poe_market_two_hand_axe USING btree (market_item_stash_uuid);


--
-- TOC entry 2593 (class 1259 OID 4988210)
-- Name: market_item_two_hand_mace_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_two_hand_mace_stash_ndx ON public.db_poe_market_two_hand_mace USING btree (market_item_stash_uuid);


--
-- TOC entry 2596 (class 1259 OID 4988224)
-- Name: market_item_two_hand_sword_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_two_hand_sword_stash_ndx ON public.db_poe_market_two_hand_sword USING btree (market_item_stash_uuid);


--
-- TOC entry 2599 (class 1259 OID 4988238)
-- Name: market_item_unarmed_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_unarmed_stash_ndx ON public.db_poe_market_unarmed USING btree (market_item_stash_uuid);


--
-- TOC entry 2602 (class 1259 OID 4988252)
-- Name: market_item_uniquefragment_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_uniquefragment_stash_ndx ON public.db_poe_market_uniquefragment USING btree (market_item_stash_uuid);


--
-- TOC entry 2605 (class 1259 OID 4988266)
-- Name: market_item_utilityflask_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_utilityflask_stash_ndx ON public.db_poe_market_utilityflask USING btree (market_item_stash_uuid);


--
-- TOC entry 2608 (class 1259 OID 4988280)
-- Name: market_item_utilityflaskcritical_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_utilityflaskcritical_stash_ndx ON public.db_poe_market_utilityflaskcritical USING btree (market_item_stash_uuid);


--
-- TOC entry 2613 (class 1259 OID 4988294)
-- Name: market_item_wand_stash_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX market_item_wand_stash_ndx ON public.db_poe_market_wand USING btree (market_item_stash_uuid);


--
-- TOC entry 2616 (class 1259 OID 4991038)
-- Name: poe_account_name_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX poe_account_name_ndx ON public.db_poe_account USING btree (poe_account_name);


--
-- TOC entry 2421 (class 1259 OID 4978161)
-- Name: poe_stash_account_uuid_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX poe_stash_account_uuid_ndx ON public.db_poe_stashes USING btree (poe_stash_account_uuid);


--
-- TOC entry 2422 (class 1259 OID 4982828)
-- Name: poe_stash_league_uuid_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX poe_stash_league_uuid_ndx ON public.db_poe_stashes USING btree (poe_league_uuid);


--
-- TOC entry 2423 (class 1259 OID 4978171)
-- Name: poe_stash_uuid_ndx; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX poe_stash_uuid_ndx ON public.db_poe_stashes USING btree (poe_stash_uuid);


--
-- TOC entry 2424 (class 1259 OID 29519)
-- Name: unique_stash; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX unique_stash ON public.db_poe_stashes USING btree (poe_stash_id_uuid);


--
-- TOC entry 2678 (class 2606 OID 4996222)
-- Name: db_poe_account_items db_poe_account_items_db_poe_account_item_class_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_account_items
    ADD CONSTRAINT db_poe_account_items_db_poe_account_item_class_uuid_fkey FOREIGN KEY (db_poe_account_item_class_uuid) REFERENCES public.db_poe_item_subtypes(item_subtype_uuid);


--
-- TOC entry 2677 (class 2606 OID 4996217)
-- Name: db_poe_account_items db_poe_account_items_db_poe_account_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_account_items
    ADD CONSTRAINT db_poe_account_items_db_poe_account_uuid_fkey FOREIGN KEY (db_poe_account_uuid) REFERENCES public.db_poe_account(poe_account_uuid);


--
-- TOC entry 2676 (class 2606 OID 4991047)
-- Name: db_poe_character db_poe_character_db_poe_account_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_character
    ADD CONSTRAINT db_poe_character_db_poe_account_uuid_fkey FOREIGN KEY (db_poe_account_uuid) REFERENCES public.db_poe_account(poe_account_uuid);


--
-- TOC entry 2622 (class 2606 OID 4976306)
-- Name: db_poe_item_subtypes db_poe_item_subtypes_db_poe_item_subtype_class_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_item_subtypes
    ADD CONSTRAINT db_poe_item_subtypes_db_poe_item_subtype_class_uuid_fkey FOREIGN KEY (db_poe_item_subtype_class_uuid) REFERENCES public.db_poe_item_class(item_class_uuid) ON DELETE CASCADE;


--
-- TOC entry 2623 (class 2606 OID 4987561)
-- Name: db_poe_market_abyssjewel db_poe_market_abyssjewel_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_abyssjewel
    ADD CONSTRAINT db_poe_market_abyssjewel_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2624 (class 2606 OID 4987575)
-- Name: db_poe_market_active_skill_gem db_poe_market_active_skill_gem_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_active_skill_gem
    ADD CONSTRAINT db_poe_market_active_skill_gem_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2625 (class 2606 OID 4987589)
-- Name: db_poe_market_amulet db_poe_market_amulet_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_amulet
    ADD CONSTRAINT db_poe_market_amulet_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2626 (class 2606 OID 4987603)
-- Name: db_poe_market_belt db_poe_market_belt_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_belt
    ADD CONSTRAINT db_poe_market_belt_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2627 (class 2606 OID 4987617)
-- Name: db_poe_market_body_armour db_poe_market_body_armour_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_body_armour
    ADD CONSTRAINT db_poe_market_body_armour_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2628 (class 2606 OID 4987631)
-- Name: db_poe_market_boots db_poe_market_boots_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_boots
    ADD CONSTRAINT db_poe_market_boots_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2629 (class 2606 OID 4987645)
-- Name: db_poe_market_bow db_poe_market_bow_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_bow
    ADD CONSTRAINT db_poe_market_bow_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2630 (class 2606 OID 4987659)
-- Name: db_poe_market_claw db_poe_market_claw_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_claw
    ADD CONSTRAINT db_poe_market_claw_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2631 (class 2606 OID 4987673)
-- Name: db_poe_market_currency db_poe_market_currency_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_currency
    ADD CONSTRAINT db_poe_market_currency_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2632 (class 2606 OID 4987687)
-- Name: db_poe_market_dagger db_poe_market_dagger_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_dagger
    ADD CONSTRAINT db_poe_market_dagger_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2633 (class 2606 OID 4987701)
-- Name: db_poe_market_delvesocketablecurrency db_poe_market_delvesocketablecurren_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_delvesocketablecurrency
    ADD CONSTRAINT db_poe_market_delvesocketablecurren_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2634 (class 2606 OID 4987715)
-- Name: db_poe_market_divinationcard db_poe_market_divinationcard_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_divinationcard
    ADD CONSTRAINT db_poe_market_divinationcard_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2635 (class 2606 OID 4987729)
-- Name: db_poe_market_fishingrod db_poe_market_fishingrod_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_fishingrod
    ADD CONSTRAINT db_poe_market_fishingrod_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2636 (class 2606 OID 4987743)
-- Name: db_poe_market_gloves db_poe_market_gloves_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_gloves
    ADD CONSTRAINT db_poe_market_gloves_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2637 (class 2606 OID 4987757)
-- Name: db_poe_market_helmet db_poe_market_helmet_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_helmet
    ADD CONSTRAINT db_poe_market_helmet_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2638 (class 2606 OID 4987771)
-- Name: db_poe_market_hideoutdoodad db_poe_market_hideoutdoodad_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_hideoutdoodad
    ADD CONSTRAINT db_poe_market_hideoutdoodad_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2639 (class 2606 OID 4987785)
-- Name: db_poe_market_hybridflask db_poe_market_hybridflask_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_hybridflask
    ADD CONSTRAINT db_poe_market_hybridflask_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2640 (class 2606 OID 4987799)
-- Name: db_poe_market_incursionitem db_poe_market_incursionitem_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_incursionitem
    ADD CONSTRAINT db_poe_market_incursionitem_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2641 (class 2606 OID 4987813)
-- Name: db_poe_market_jewel db_poe_market_jewel_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_jewel
    ADD CONSTRAINT db_poe_market_jewel_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2642 (class 2606 OID 4987827)
-- Name: db_poe_market_labyrinthitem db_poe_market_labyrinthitem_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_labyrinthitem
    ADD CONSTRAINT db_poe_market_labyrinthitem_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2643 (class 2606 OID 4987841)
-- Name: db_poe_market_labyrinthmapitem db_poe_market_labyrinthmapitem_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_labyrinthmapitem
    ADD CONSTRAINT db_poe_market_labyrinthmapitem_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2644 (class 2606 OID 4987855)
-- Name: db_poe_market_labyrinthtrinket db_poe_market_labyrinthtrinket_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_labyrinthtrinket
    ADD CONSTRAINT db_poe_market_labyrinthtrinket_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2645 (class 2606 OID 4987869)
-- Name: db_poe_market_largerelic db_poe_market_largerelic_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_largerelic
    ADD CONSTRAINT db_poe_market_largerelic_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2646 (class 2606 OID 4987883)
-- Name: db_poe_market_leaguestone db_poe_market_leaguestone_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_leaguestone
    ADD CONSTRAINT db_poe_market_leaguestone_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2647 (class 2606 OID 4987897)
-- Name: db_poe_market_lifeflask db_poe_market_lifeflask_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_lifeflask
    ADD CONSTRAINT db_poe_market_lifeflask_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2648 (class 2606 OID 4987911)
-- Name: db_poe_market_manaflask db_poe_market_manaflask_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_manaflask
    ADD CONSTRAINT db_poe_market_manaflask_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2649 (class 2606 OID 4987925)
-- Name: db_poe_market_map db_poe_market_map_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_map
    ADD CONSTRAINT db_poe_market_map_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2650 (class 2606 OID 4987939)
-- Name: db_poe_market_mapfragment db_poe_market_mapfragment_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_mapfragment
    ADD CONSTRAINT db_poe_market_mapfragment_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2651 (class 2606 OID 4987953)
-- Name: db_poe_market_mediumrelic db_poe_market_mediumrelic_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_mediumrelic
    ADD CONSTRAINT db_poe_market_mediumrelic_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2652 (class 2606 OID 4987967)
-- Name: db_poe_market_microtransaction db_poe_market_microtransaction_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_microtransaction
    ADD CONSTRAINT db_poe_market_microtransaction_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2653 (class 2606 OID 4987981)
-- Name: db_poe_market_miscmapitem db_poe_market_miscmapitem_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_miscmapitem
    ADD CONSTRAINT db_poe_market_miscmapitem_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2654 (class 2606 OID 4987995)
-- Name: db_poe_market_one_hand_axe db_poe_market_one_hand_axe_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_one_hand_axe
    ADD CONSTRAINT db_poe_market_one_hand_axe_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2655 (class 2606 OID 4988009)
-- Name: db_poe_market_one_hand_mace db_poe_market_one_hand_mace_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_one_hand_mace
    ADD CONSTRAINT db_poe_market_one_hand_mace_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2656 (class 2606 OID 4988023)
-- Name: db_poe_market_one_hand_sword db_poe_market_one_hand_sword_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_one_hand_sword
    ADD CONSTRAINT db_poe_market_one_hand_sword_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2657 (class 2606 OID 4988037)
-- Name: db_poe_market_pantheonsoul db_poe_market_pantheonsoul_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_pantheonsoul
    ADD CONSTRAINT db_poe_market_pantheonsoul_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2658 (class 2606 OID 4988051)
-- Name: db_poe_market_questitem db_poe_market_questitem_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_questitem
    ADD CONSTRAINT db_poe_market_questitem_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2659 (class 2606 OID 4988065)
-- Name: db_poe_market_quiver db_poe_market_quiver_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_quiver
    ADD CONSTRAINT db_poe_market_quiver_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2660 (class 2606 OID 4988079)
-- Name: db_poe_market_ring db_poe_market_ring_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_ring
    ADD CONSTRAINT db_poe_market_ring_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2661 (class 2606 OID 4988093)
-- Name: db_poe_market_sceptre db_poe_market_sceptre_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_sceptre
    ADD CONSTRAINT db_poe_market_sceptre_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2662 (class 2606 OID 4988107)
-- Name: db_poe_market_shield db_poe_market_shield_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_shield
    ADD CONSTRAINT db_poe_market_shield_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2663 (class 2606 OID 4988121)
-- Name: db_poe_market_smallrelic db_poe_market_smallrelic_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_smallrelic
    ADD CONSTRAINT db_poe_market_smallrelic_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2664 (class 2606 OID 4988135)
-- Name: db_poe_market_stackablecurrency db_poe_market_stackablecurrency_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_stackablecurrency
    ADD CONSTRAINT db_poe_market_stackablecurrency_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2665 (class 2606 OID 4988149)
-- Name: db_poe_market_staff db_poe_market_staff_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_staff
    ADD CONSTRAINT db_poe_market_staff_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2666 (class 2606 OID 4988163)
-- Name: db_poe_market_support_skill_gem db_poe_market_support_skill_gem_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_support_skill_gem
    ADD CONSTRAINT db_poe_market_support_skill_gem_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2667 (class 2606 OID 4988177)
-- Name: db_poe_market_thrusting_one_hand_sword db_poe_market_thrusting_one_hand_sw_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_thrusting_one_hand_sword
    ADD CONSTRAINT db_poe_market_thrusting_one_hand_sw_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2668 (class 2606 OID 4988191)
-- Name: db_poe_market_two_hand_axe db_poe_market_two_hand_axe_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_two_hand_axe
    ADD CONSTRAINT db_poe_market_two_hand_axe_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2669 (class 2606 OID 4988205)
-- Name: db_poe_market_two_hand_mace db_poe_market_two_hand_mace_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_two_hand_mace
    ADD CONSTRAINT db_poe_market_two_hand_mace_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2670 (class 2606 OID 4988219)
-- Name: db_poe_market_two_hand_sword db_poe_market_two_hand_sword_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_two_hand_sword
    ADD CONSTRAINT db_poe_market_two_hand_sword_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2671 (class 2606 OID 4988233)
-- Name: db_poe_market_unarmed db_poe_market_unarmed_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_unarmed
    ADD CONSTRAINT db_poe_market_unarmed_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2672 (class 2606 OID 4988247)
-- Name: db_poe_market_uniquefragment db_poe_market_uniquefragment_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_uniquefragment
    ADD CONSTRAINT db_poe_market_uniquefragment_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2673 (class 2606 OID 4988261)
-- Name: db_poe_market_utilityflask db_poe_market_utilityflask_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_utilityflask
    ADD CONSTRAINT db_poe_market_utilityflask_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2674 (class 2606 OID 4988275)
-- Name: db_poe_market_utilityflaskcritical db_poe_market_utilityflaskcritical_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_utilityflaskcritical
    ADD CONSTRAINT db_poe_market_utilityflaskcritical_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


--
-- TOC entry 2675 (class 2606 OID 4988289)
-- Name: db_poe_market_wand db_poe_market_wand_market_item_stash_uuid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.db_poe_market_wand
    ADD CONSTRAINT db_poe_market_wand_market_item_stash_uuid_fkey FOREIGN KEY (market_item_stash_uuid) REFERENCES public.db_poe_stashes(poe_stash_uuid) ON DELETE CASCADE;


-- Completed on 2019-04-18 19:52:21

--
-- PostgreSQL database dump complete
--

