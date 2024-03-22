import React, {useState} from 'react';
import { Table, Button, Icon} from "semantic-ui-react";
import './TableSites.scss';
import { map } from "lodash";
import {usePing} from "../../../../hooks/usePing";


export function TableSites(props) {
    const { sites, updateSite, onDeleteSite,  } = props
    console.log(sites)
    return (
        <Table>
            <Table.Header>
                <Table.Row>
                    <Table.HeaderCell>Site name</Table.HeaderCell>
                    <Table.HeaderCell>Region</Table.HeaderCell>
                    <Table.HeaderCell>Country</Table.HeaderCell>
                    <Table.HeaderCell>City</Table.HeaderCell>
                    <Table.HeaderCell>Administrator</Table.HeaderCell>
                    <Table.HeaderCell>Devices</Table.HeaderCell>
                    <Table.HeaderCell></Table.HeaderCell>
                </Table.Row>
            </Table.Header>
            <Table.Body>
                {map(sites, (site, index) =>(
                    <Table.Row key={index}>
                        <Table.Cell>{site.site_name}</Table.Cell>
                        <Table.Cell>{site.region}</Table.Cell>
                        <Table.Cell>{}</Table.Cell>
                        <Table.Cell>{site.city}</Table.Cell>
                        <Table.Cell>{site.administrator !== null ? (site.administrator.email !== null ? site.administrator.email : "Administrator not assigned") : "Administrator not assigned"}</Table.Cell>
                        <Table.Cell>{site.devices}</Table.Cell>
                        <Table.Cell>
                            <Actions site_act={site} updateSite={updateSite} onDeleteSite={onDeleteSite}/>
                        </Table.Cell>
                    </Table.Row>
                ))}
            </Table.Body>
        </Table>
    );
}

function Actions(props) {
    const { site_act, updateSite, onDeleteSite,  } = props;
    const [isLoadingPing, setIsLoadingPing] = useState(false);
    const [pingResults, setPingResults] = useState([]);
    const { ping, getPing } = usePing()
    const handlePingClick = async (site_id) => {
        try {
            setIsLoadingPing(true);
        } catch (error) {
            console.error('Error:', error);
        } finally {
            setIsLoadingPing(false);
        }
    };

    return (
        <>
            <Table.Cell textAlign="right">
                <Button icon loading={isLoadingPing} onClick={() => handlePingClick()}>
                    <Icon name="play" color={pingResults !== null ? (pingResults ? "green" : "red") : "grey"} />
                </Button>
                <Button icon onClick={() => updateSite(site_act)}>
                    <Icon name="pencil" />
                </Button>
                <Button icon negative onClick={() => onDeleteSite(site_act)}>
                    <Icon name="close" />
                </Button>
            </Table.Cell>
        </>
    );
}