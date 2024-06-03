/*
GroundX API

Ground Your RAG Apps in Fact not Fiction

The version of the OpenAPI document: 1.0.0
Contact: support@groundx.ai

NOTE: This file is auto generated by Konfig (https://konfigthis.com).
*/

import { AxiosRequestConfig } from "axios";
import {
  BucketsApi,
  DocumentsApi,
  HealthApi,
  ProjectsApi,
  SearchApi,
} from "./api";
import { Configuration, ConfigurationParameters } from "./configuration";
import { GroundxCustom } from "./client-custom";

export class Groundx extends GroundxCustom {
  readonly buckets: BucketsApi;
  readonly documents: DocumentsApi;
  readonly health: HealthApi;
  readonly projects: ProjectsApi;
  readonly search: SearchApi;

  constructor(configurationParameters: ConfigurationParameters) {
    super(configurationParameters);
    const configuration = new Configuration(configurationParameters);
    this.buckets = new BucketsApi(configuration);
    this.documents = new DocumentsApi(configuration);
    this.health = new HealthApi(configuration);
    this.projects = new ProjectsApi(configuration);
    this.search = new SearchApi(configuration);
  }

}
